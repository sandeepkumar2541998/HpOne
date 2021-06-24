from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("electricbikes",views.electricbikes,name="electricbikes"),
    path("electriccars",views.electriccars,name="electriccars"),
]
