from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.landing, name="landing"),
    path('home',views.home, name="home"),
    path('index',views.index,name="index"),
]
