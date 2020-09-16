from django.contrib import admin
from django.urls import path


from news import views
urlpatterns = [
    path('index',views.index, name="index"),
    path('exit',views.exit ,name="exit"),
    path('ht',views.ht ,name="ht"),
    path('inshorts',views.inshorts ,name="inshorts"),
    path('toi',views.toi ,name="toi"),
    path('home',views.home ,name="home"),
    path('',views.index, name="index"),
]
