from django.shortcuts import render

# Create your views here.
def range10_50k(request):
    return render(request,'pricerange/10_50k.html')

def range50_70k(request):
    return render(request,'pricerange/50_70k.html')

def range70k_1lakh(request):
    return render(request,'pricerange/70k_1lakh.html')

def range1_2lakh(request):
    return render(request,'pricerange/1_2lakh.html')

def range2_5lakh(request):
    return render(request,'pricerange/2_5lakh.html')

def rangeabove_5lakh(request):
    return render(request,'pricerange/above_5lakh.html')