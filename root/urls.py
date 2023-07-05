from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('base/', views.base),
    path('about/', views.about,name="about"),
    path('client/', views.client,name="client"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('signin/', views.signin,name="signin"),
    path('customers/', views.customers),
    path('clientprofile/', views.clientprofile,name="clientprofile"),
    path('booking/', views.clientbooking, name="cbook"),
    path('customerLogin/',views.custlogin,name="custlogin"),
    path('customerSignin/',views.custsignin,name="custsignin"),
    path('customerlogout/', views.custlogout,name='custlogout'),
    path('requirements/<str:name>/',views.require,name="require"),
    path('showbooking/',views.showbooking,name="showbooking"),
    path('confirmed/<str:id>/',views.confApp,name="confirm"),
    path('rejected/<str:id>/',views.rejApp,name="rejected"),
    path('update/',views.updateprofile,name="updateprofile")
]