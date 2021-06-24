from django.shortcuts import render

# Create your views here.
def recommended(request):
    return render(request,'carbikeupdates/recommended.html')


def featured(request):
    return render(request,'carbikeupdates/featured.html')

def latest(request):
    return render(request,'carbikeupdates/latest.html')

def reviews(request):
    return render(request,'carbikeupdates/reviews.html')

def videos(request):
    return render(request,'carbikeupdates/videos.html')