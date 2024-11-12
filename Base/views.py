from django.http import HttpResponse

from django.shortcuts import render
from Blogs.models import *

def index(request):
    choices=STATUS_CHOICES
    print(type(choices))
    for k,v in choices.items():
        print(v)
    
    return render(request,'frontend/pages/index.html')




