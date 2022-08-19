from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register', views.register, name='register'),
    path('registerhandle', views.registerhandle, name='registerhandle'),
path('userpage', views.userpage, name='userpage'),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handelLogoutt"),
    path('hairstyle/', views.hairstyle, name='hairstyle'),
    path('haircut/', views.haircut, name='haircut'),
    path('beard/', views.beard, name='beard'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointmenthandle/', views.appointmenthandle, name='appointmenthandle'),

]
