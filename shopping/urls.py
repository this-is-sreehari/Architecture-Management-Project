from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.sellerLogin,name='sellerLogin'),
    path('signin/',views.sellerSignin,name='sellerSignin'),
    path('addProduct/',views.addProduct,name='addProduct'),
    path('logout/',views.logout,name='sellerLogout'),
    path('bookProduct/',views.prodBooking,name='prodBooking'),
    path('customerLogin/',views.customerLogin,name='customerLogin'),
    path('customerSignIn/',views.customerSignin,name='customerSignin'),
    path('addTocart/<int:product_id>/', views.addToCart, name='addToCart'),
    path('cart/', views.cart, name='cart'),
    path('removeFromCart/<int:cart_id>/', views.removeFromCart, name='removeFromCart'),
    path('Orders/',views.orders,name='orders'),
]