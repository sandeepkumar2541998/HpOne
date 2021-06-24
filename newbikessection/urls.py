from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("morepopularbikes",views.morepopularbikes, name="morepopularbikes"),
    path("latest",views.latest,name="latest"),
    path("upcoming",views.upcoming,name="upcoming"),
]
