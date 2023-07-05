from django import forms

from .models import Products

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