from django.shortcuts import render
from .models import Recommended,Supercars,Carbrands
# Create your views here.
def index(request):
    bikes = Recommended.objects.all()
    cars = Supercars.objects.all()
    carbrands = Carbrands.objects.all()
    return render(request,'index.html',{'bikes':bikes,'cars':cars,'carbrands':carbrands})

def community(request):
    return render(request,'community.html')