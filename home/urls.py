from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [ 
    path('index',views.index, name="home"),
    path('Carts',views.Carts,name="Carts"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('shop',views.shop,name="shop"),
    path('signout',views.signout,name="signout"),
    path('signin',views.signin,name="signin"),
]
