from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("range10_50k",views.range10_50k,name="range10_50k"),
    path("range50_70k",views.range50_70k,name="range50_70k"),
    path("range70k_1lakh",views.range70k_1lakh,name="range70k_1lakh"),
    path("range1_2lakh",views.range1_2lakh,name="range1_2lakh"),
    path("range2_5lakh",views.range2_5lakh,name="range2_5lakh"),
    path("rangeabove_5lakh",views.rangeabove_5lakh,name="rangeabove_5lakh"),
]
