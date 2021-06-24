from django.shortcuts import render

# Create your views here.
def popular(request):
    return render(request,'newcars/popular.html')

def latest(request):
    return render(request,'newcars/latest.html')

def upcoming(request):
    return render(request,'newcars/upcoming.html')