from django import forms

from .models import Products,Purchase

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        labels ={
            'name':'Enter Product Name',
            'price':'Enter Price',
            'category':'Enter Category',
            'description':'Enter Description',
            'image':'Upload Image',
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        labels = {
            'name':'Your Name',
            'mob':'Mobile Number',
            'mail':'Mail ID',
            'add1':'Address Line 1',
            'add2':'Address Line 2',
            'pin':'PIN Code',
            'payment':'Payment Mode',
            'amnt':'Net Amount'
        }
        exclude = ['bookid','dtime']

        