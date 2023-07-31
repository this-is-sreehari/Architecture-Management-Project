from django.contrib import admin

from .models import Category,Cart,Customer,Products,Purchase

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('user','name','price','category','description','image')
class CartAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity','price')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('bookid','dtime','name','mob','mail','add1','add2','pin','items','payment','amnt')

admin.site.register(Category)
admin.site.register(Cart,CartAdmin)
admin.site.register(Customer)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Purchase,PurchaseAdmin)