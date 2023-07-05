from django.contrib import admin
from .models import CProfile,Booking,Requirements
# Register your models here.

class CProfileAdmin(admin.ModelAdmin):
    list_display = ('c_name','loc','m_name','s_year','contact','mail','y_link','pic1','pic2','pic3')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('proj_id','name','mobno','loc','client','mail')


class ReqAdmin(admin.ModelAdmin):
    list_display=('uname','proj_id','plot_area','type','sqft','place','location','requirement','budget')


admin.site.register(CProfile,CProfileAdmin)

admin.site.register(Booking,BookingAdmin)

admin.site.register(Requirements,ReqAdmin)