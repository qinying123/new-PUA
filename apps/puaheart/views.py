from django.shortcuts import render

def choose(request):
    return render(request, 'puaheart/choose.html')

def one(request):
    return render(request,'puaheart/index1.html')

def two(request):
    return render(request,'puaheart/index2.html')