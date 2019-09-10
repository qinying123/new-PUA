from django.shortcuts import render

def baike_index(request):
    return render(request,'puabaike/bk-index.html')