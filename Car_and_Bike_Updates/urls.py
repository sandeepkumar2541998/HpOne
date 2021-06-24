from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("recommended",views.recommended,name="recommended"),
    path("featured",views.featured,name="featured"),
    path("latest",views.latest,name="latest"),
    path("reviews",views.reviews,name="reviews"),
    path("videos",views.videos,name="videos"),
]
