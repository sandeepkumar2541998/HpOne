from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("facebook",views.facebook,name="facebook"),
    path("instagram",views.instagram,name="instagram"),
    path("twitter",views.twitter,name="twitter"),
    path("whatsapp",views.whatsapp,name="whatsapp"),
]
