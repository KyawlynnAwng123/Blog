from django.http import HttpResponse
from django.shortcuts import render
from Blogs.models import *

def index(request):
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True,status='1').order_by('-updated')
    posts=Blog.objects.filter(is_featured=False,status='1')
    
   
    
    context={
        'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts
        
        }
    return render(request,'frontend/pages/index.html',context)




