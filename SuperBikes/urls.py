from django.contrib import admin
from django.urls import path
from SuperBikes import views


urlpatterns = [
    path("",views.index,name="index"),
    path("community",views.community,name="community"),
]
