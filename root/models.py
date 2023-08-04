from django.db import models

# Create your models here.

class CProfile(models.Model):
    cl_id = models.CharField(max_length=10)
    c_name = models.CharField(max_length=255)
    loc = models.CharField(max_length=255)
    opt = [
        ('Designing','Designing Project'),
        ('Constructing','Constructing Project'),
        ('Designing And Construction','Designing And Construction')
    ]
    dom = models.CharField(max_length=50,choices=opt)
    m_name = models.CharField(max_length=255)
    s_year = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    mail = models.EmailField()
    y_link = models.URLField(max_length=200,null=True,blank=True)
    pic1 = models.ImageField(null=True,blank=True,upload_to="images/")
    pic2 = models.ImageField(null=True,blank=True,upload_to="images/")
    pic3 = models.ImageField(null=True,blank=True,upload_to="images/")
    
    def __str__(self):
        return self.c_name
    
class Booking(models.Model):
    proj_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    mobno = models.IntegerField()
    loc = models.CharField(max_length=100)
    client = models.ForeignKey(CProfile,on_delete=models.CASCADE)
    mail = models.EmailField()

    def __str__(self):
        return self.name
    
class Requirements(models.Model):
    uname = models.CharField(max_length=20)
    proj_id = models.CharField(max_length=10)
    plot_area = models.DecimalField(max_digits=6,decimal_places=2)
    opt =[
        ('Single_Normal','Single Storied - Normal'),
        ('Double_Normal','Double Storied - Normal'),
        ('Modern_Style','Modern Architecture'),
        ('Traditional_Style','Traditional Kerala Architecture'),
        ('Colonial_Style','Colonial Architecture'),
        ('Dutch_Style','Dutch Architecture'),
        ('Victorian_Style','Victorian Architecture')
    ]
    type = models.CharField(max_length=40,choices=opt)
    sqft = models.IntegerField()
    place = models.CharField(max_length=20)
    location = models.URLField(max_length=200)
    requirement = models.TextField(max_length=500)
    budget = models.IntegerField()

    def __str__(self):
        return self.proj_id
