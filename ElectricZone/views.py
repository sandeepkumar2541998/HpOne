from django.shortcuts import render

# Create your views here.
def electricbikes(request):
    return render(request,'electriczone/electricbikes.html')

def electriccars(request):
    return render(request,'electriczone/electriccars.html')