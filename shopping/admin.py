from django.contrib import admin

from .models import Category,Cart,Customer,Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','description','image')
class CartAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity','price')

admin.site.register(Category)
admin.site.register(Cart,CartAdmin)
admin.site.register(Customer)
admin.site.register(Products,ProductsAdmin)