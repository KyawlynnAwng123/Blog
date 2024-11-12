from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request,'frontend/pages/index.html')




