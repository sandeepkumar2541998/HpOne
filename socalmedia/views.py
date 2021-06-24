from django.shortcuts import render

# Create your views here.
def facebook(request):
    return render(request,'socalmedia/facebook.html')

def instagram(request):
    return render(request,'socalmedia/instagram.html')

def twitter(request):
    return render(request,'socalmedia/twitter.html')

def whatsapp(request):
    return render(request,'socalmedia/whatsapp.html')