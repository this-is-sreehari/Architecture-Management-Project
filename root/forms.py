from django import forms
#from django.forms.widgets import RadioSelect

from .models import CProfile,Booking,Requirements

class CPForm(forms.ModelForm):
    class Meta:
        model = CProfile
        fields = '__all__'
        labels ={
            'c_name':'Company Name',
            'loc':'Location',
            'm_name':'Manager Name',
            's_year':'Starting Year',
            'contact':'Contact Number',
            'mail':'Mail ID',
            'y_link':'Youtube Link',
            'pic1':'Sample Image of Recent Work 1',
            'pic2':'Sample Image of Recent Work 2',
            'pic3':'Sample Image of Recent Work 3',

        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        labels = {
            'proj_id':'Project ID',
            'name':'Name',
            'mobno':'Contact Number',
            'loc' : 'Location',
            'client' : 'Client',
            'mail':'Mail ID',
        }

class ReqForm(forms.ModelForm):
    class Meta:
        model = Requirements
        fields = '__all__'
        labels = {
            'uname':'User Name',
            'proj_id':'Project ID',
            'plot_area':'Plot Area (In Cents)',
            'type':'Single Storied or Double Storied',
            'sqft':'Estimated Square Ft.',
            'place':'Place of Customer',
            'location':'Plot Location (Share location as link)',
            'requirement':'Your Requirements',
            'budget':'Budget (in Lakhs INR)',
        }
        
class SearchForm(forms.Form):
    Project_ID = forms.CharField(max_length=10,required=True)