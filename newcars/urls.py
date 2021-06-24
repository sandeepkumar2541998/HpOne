from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("popular",views.popular,name="popular"),
    path("latest",views.latest,name="latest"),
    path("upcoming",views.upcoming,name="upcoming"),
]
