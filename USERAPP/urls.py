from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('single/<int:id>/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('publicdata/', views.publicdata, name='publicdata'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('customerdata/', views.customerdata, name='customerdata'),
    path('registerdata/', views.registerdata, name='registerdata'),
    path('products/<str:category>', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
    path('booking/', views.booking, name='booking'),
    path('bookingdata/', views.bookingdata, name='bookingdata'),
    path('ordered/', views.ordered, name='ordered'),
    path('cartdata/<int:id>/', views.cartdata, name='cartdata'),
    path('cart/', views.cart, name='cart'),
    path('cartdelete/<int:id>', views.cartdelete, name='cartdelete'),
    path('history/', views.history, name='history'),
    path('complaint/<int:id>/', views.complaint, name='complaint'),
    path('complaintdata/<int:id>/', views.complaintdata, name='complaintdata'),
    path('payment_success', views.payment_success, name='payment_success'),
   
       
]
