from django.shortcuts import render,redirect
from .models import Products,Cart,Purchase
from .forms import ProductForm,PurchaseForm
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import socket,random,datetime

# Create your views here.

def home(request):
    try:
        # items = Cart.objects.filter(user = request.user).values_list('quantity',flat=True).first()
        items = {
        'tot_items':0
        }
        items = Cart.objects.filter(user = request.user).aggregate(tot_items=Sum('quantity'))       
        if items is None:
            items['tot_items']=0
        products = {
        'products':Products.objects.all(),
        'items':items['tot_items']
        }
    except TypeError:
        pass
    
    products = {
        'products':Products.objects.all(),
        'items':items['tot_items']
    }
    return render(request,'shop/index.html',products)

def sellerLogin(request): 
    if request.method== 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        user = auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request, user)
            return render(request,'shop/sellerHome.html')
        else:
            messages.info(request, 'Invalid Username or Password')
            return render(sellerLogin)
    else:
        return render(request, 'shop/login.html')

def sellerlogout(request):
    auth.logout(request)
    return redirect(sellerLogin)

def sellerSignin(request):
    if request.method == 'POST':
        u_name = request.POST['u_name']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        phone = request.POST['phone']
        email = request.POST['email']
        pwd = request.POST['pwd']
        rpwd = request.POST['rpwd']
        if pwd == rpwd:
            if User.objects.filter(username=u_name).exists():
                messages.info(request, 'username already exist')
                return redirect(sellerSignin)
            else:
                user = User.objects.create_user(username=u_name,first_name=f_name,
                                                last_name=l_name,password=pwd,email=email)
                user.set_password(pwd)
                user.save()
                return redirect(sellerLogin)
    else:
        return render(request,'shop/signin.html')

def addProduct(request):
    if request.method=="POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request,"Successfully Added The Product!")
            return render(request,'shop/addProduct.html')
    form = ProductForm()
    dict_form = {
        'form':form
    }
    return render(request,'shop/addProduct.html',dict_form)

def prodBooking(request): 
    products = {
        'products':Products.objects.all()
         }
    return render(request,'shop/productBooking.html',products)

def customerLogin(request):
    if request.method== 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        user = auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
           
        else:
            messages.info(request, 'Invalid Username or Password')
            return render(customerLogin)
    else:
        return render(request, 'shop/customerLogin.html')

def customerSignin(request):
    if request.method == 'POST':
        u_name = request.POST['u_name']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        pwd = request.POST['pwd']
        rpwd = request.POST['rpwd']
        if pwd == rpwd:
            if User.objects.filter(username=u_name).exists():
                messages.info(request, 'username already exist')
                return redirect(customerLogin)
            else:
                user = User.objects.create_user(username=u_name,first_name=f_name,
                                                last_name=l_name,password=pwd)
                user.set_password(pwd)
                user.save()
                return redirect(customerLogin)
    else:
        return render(request,'shop/customerSignin.html')

def custlogout(request):
    auth.logout(request)
    return redirect(customerLogin)
    
@login_required
def addToCart(request,product_id):
    product = Products.objects.get(pk=product_id)
    price = Products.objects.filter(id=product_id).values_list('price',flat=True)
    amount = int(price[0])
    cart_item, created = Cart.objects.get_or_create(user = request.user , product = product)
    cart_item.quantity += 1
    cart_item.price += amount
    cart_item.save()
    return redirect('home')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user = request.user)
    print(type(cart_items))
    cart_sum = Cart.objects.filter(user = request.user).aggregate(total=Sum('price'))['total']
    return render(request, 'shop/cart.html', {'cart_items':cart_items,'total':cart_sum})
    

def removeFromCart(request,cart_id):
    cart_item = Cart.objects.get(pk=cart_id)
    cart_item.delete()
    return redirect('cart')

def purchase(request,sum):
    amount = sum 
    rand = random.randint(100000,999999)
    bid = f'BID{rand}'
    cart_items = Cart.objects.filter(user = request.user)
    it_lis=[]

    for it in cart_items:
        val = f'{it.product.name}-{it.quantity}'
        it_lis.append(val)
        
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.instance.bookid = bid
            form.instance.dtime = datetime.datetime.now()
            form.instance.items = ','.join(it_lis)
            form.save()
            try:
                name=request.POST['name']
                to_mail=request.POST['mail']
                sender = settings.EMAIL_HOST_USER
                sub="Eco Dots: Order placed!"
                msg=f"Dear {name},\nYour order is successfully placed with Booking ID {bid}. Items will be shipped immediately.\nThank You"
                send_mail(sub,msg,sender,[to_mail])
            except socket.gaierror as e:
                print(e)
            messages.success(request,"Congrats, Your Order Has Been Placed!")
            return render(request,'shop/purchase.html')
    form = PurchaseForm(initial={'amnt':amount})
    return render(request,'shop/purchase.html',{'form':form})
    #return HttpResponse("Order confirmation page")


