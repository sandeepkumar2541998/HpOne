from django.shortcuts import render

# Create your views here.
def morepopularbikes(request):
    return render(request,'newbikessection/morepopularbikes.html')

def latest(request):
    return render(request,'newbikessection/latest.html')

def upcoming(request):
    return render(request,'newbikessection/upcoming.html')