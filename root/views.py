from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import CPForm,BookingForm,ReqForm,SearchForm,UpdateForm
from .models import CProfile,Requirements,Booking
from django.core.mail import send_mail
from django.conf import settings
import socket,random
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'client/index.html')

def about(request):
    return render(request, 'client/about.html')

def client(request):
    dict_client={
      'clients': CProfile.objects.all()
    }
    return render(request,'client/client.html',dict_client)


def login(request):           
        if request.method== 'POST':
            c_name = request.POST['c_name']
            pwd = request.POST['pwd']
            try:
                user = auth.authenticate(username=c_name,password=pwd)
            except:
                pass
            if user is not None:
                auth.login(request, user)
                return render(request,'client/clienthome.html')
            else:
                messages.info(request, 'Invalid Username or Password')
                return render(request, 'client/login.html')
        else:
            return render(request, 'client/login.html')
        
def logout(request):
    auth.logout(request)
    return redirect(login)

def customers(request):
    return render(request, 'client/customers.html')

def base(request):
    return render(request, 'client/base.html')

def signin(request):
    if request.method == 'POST':
        c_name = request.POST['c_name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        rpwd = request.POST['rpwd']
        if pwd == rpwd:
            if User.objects.filter(username=c_name).exists():
                messages.info(request, 'username already exist')
                return redirect(signin)
            else:
                user = User.objects.create_user(username=c_name,password=pwd,email=email)
                user.set_password(pwd)
                user.save()
                return redirect(login)
    else:
        return render(request,'client/signin.html')

def clientprofile(request):
    random_num = random.randint(1000000,9999999)
    cl_id = f"CLI{random_num}"
    form = CPForm(initial={'cl_id':cl_id})
    dict_form = {
        'form':form
    }
    if request.method=="POST":
        form = CPForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()           
            messages.success(request,f"Successfully Created The Profile! Your ID is '{cl_id}'.")
            return render(request,'client/clientprofile.html') 
    return render(request,'client/clientprofile.html',dict_form)

def clientbooking(request):
    pid = Requirements.objects.latest('proj_id').proj_id
    if request.method=="POST":
        form = BookingForm(request.POST)
        try:
            mail = request.POST.get('mail')
            name = request.POST.get('name')
            cid = request.POST.get('client')
            cmail = CProfile.objects.get(id=cid).mail
            print(cmail)
            subject = 'Appointment Requested'
            message = f'Dear {name},\nYour project ID is {pid}. Keep the ID safe for future references. Thank you, for being a part of Eco Dots project.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [mail]
            send_mail(subject,message,from_email,recipient_list)
            subject1 = 'Eco Dots: You have a request'
            message1 = f'An appointment request has been made. Customer name is {name} & ID is {pid}. Check your profile immediatetly.'
            recipient_list1 = [cmail]
            send_mail(subject1,message1,from_email,recipient_list1)
        except socket.gaierror as e:
                pass
        if form.is_valid():
            form.save()
            messages.success(request,"Congrats! Form Successfully Submitted")
            return render(request,'client/booking.html')
        
    form = BookingForm(initial={'proj_id':pid})
    dict_form = {
        'form':form
    }
    return render(request,'client/booking.html',dict_form)


def custlogin(request):
    if request.method== 'POST':
        c_name = request.POST['cust_name']
        pwd = request.POST['pwd']
        try:
            user = auth.authenticate(username=c_name,password=pwd)
        except:
            pass
        if user is not None:
            auth.login(request, user)
            return render(request,'client/custhome.html')
        else:
            messages.info(request, 'Invalid Username or Password')
            return render(request, 'client/customerlog.html')
    else:
        return render(request, 'client/customerlog.html')

def custsignin(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        c_name = request.POST['c_name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        rpwd = request.POST['rpwd']
        if pwd == rpwd:
            if User.objects.filter(username=c_name).exists():
                messages.info(request, 'username already exist')
                return redirect(custsignin)
            else:
                user = User.objects.create_user(username=c_name,password=pwd,email=email,first_name=f_name,last_name=l_name)
                user.set_password(pwd)
                user.save()
                return redirect(custlogin)
    else:
        return render(request,'client/customersig.html')

def custlogout(request):
    auth.logout(request)
    return redirect(custlogin)
    
def require(request,name):
    if request.method=='POST':
        form = ReqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Requirements are saved. Click on above 'Proceed Appointment' button to continue")
            return render(request,'client/req.html')
    random_num = random.randint(1000000,9999999)
    pid = f"PID{random_num}"
    u_name = name
    form = ReqForm(initial={'proj_id':pid,'uname':u_name})
    dict_form = {
        'form':form
    }
    return render(request,'client/req.html',dict_form)

def showbooking(request):
    form = SearchForm()
    items=[]
    user=[]
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            value = form.cleaned_data['Project_ID']
            try:
                user = Booking.objects.get(proj_id=value)
                items = Requirements.objects.get(proj_id__icontains=value)
            except ObjectDoesNotExist:
                pass   
    context = {
    'form':form,
    'items':items,
    'user':user
    }
    return render(request,'client/showbooking.html',context)

def confApp(request,id):
        pid = id
        name = Booking.objects.get(proj_id=pid).name
        client = Booking.objects.get(proj_id=pid).client
        cust_mail = Booking.objects.get(proj_id=pid).mail
        mob = CProfile.objects.get(c_name=client).contact
        client_mail = CProfile.objects.get(c_name=client).mail
        try:
            subject = "Eco Dots: Your request is accepted"
            message = f'Dear {name},\n{client} is interested in your project and is willing to give you an appointment.Here are the clients details;\nMobile No: +91 {mob}\nMail ID: {client_mail}.\nGive a call anytime between 10 A.M to 3 P.M (IST) or DM on whatsapp(Sooner the better!).'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [cust_mail]
            send_mail(subject,message,from_email,recipient_list)           
        except socket.gaierror as e:
            pass       
        messages.success(request,'Good job!\nThe customer will be notified immediately. Wish you all the best for this project.')
        return render(request,'client/confirm.html')
def rejApp(request,id):
        pid = id
        name = Booking.objects.get(proj_id=pid).name
        client = Booking.objects.get(proj_id=pid).client
        cust_mail = Booking.objects.get(proj_id=pid).mail
        try:
            subject = "Eco Dots: Sorry your request is turned down"
            message = f'Dear {name},\nWe are sorry to inform you that {client} is currently not in a position to take over your project. We wish you luck to find an able client to fulfill your dream project'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [cust_mail]
            send_mail(subject,message,from_email,recipient_list)
        except socket.gaierror as e:
          pass
        messages.error(request,'Thank you & please keep a watch on your inbox for further requests.')
        return render(request,'client/rejected.html')
    
def updateprofile(request):
    form = SearchForm()
    upform = UpdateForm()
    try:
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                client_id = form.cleaned_data['Project_ID']
        cl_up = get_object_or_404(CProfile,cl_id=client_id)
        if request.method == 'POST':    
            upform = UpdateForm(request.POST,instance=cl_up)
            if upform.is_valid():          
                upform.save()
                messages.success(request,"Updated Successfully!")
                return render(request,'client/updateprofile.html')
    except UnboundLocalError:
        pass
    except CProfile.DoesNotExist:
        messages.success(request,"Profile doesnt exist!")
    context = {
        'form':form,
        'upform':upform
    }
    return render(request,'client/updateprofile.html',context)
