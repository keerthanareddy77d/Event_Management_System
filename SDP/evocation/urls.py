from django.urls import path
from . import views
urlpatterns= [
     path('',views.login),
     path('home',views.home),
     path('halls',views.halls),
     path('catering',views.catering),
     path('about',views.about),
     path('registeruser',views.register),
     path('weather',views.weather,name='weather'),
     path('w',views.showweather,name='w'),
     path('qrcode/',views.qrcode12,name='qrcode1'),
     path('k/',views.qrcode3,name='k'),
     path('cards',views.cards),
     path('celebs', views.celebs),
     path('contact', views.contact,name='contact'),
     path('registerInput',views.registerInput),
     path('loginInput',views.loginInput),

]