from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Blog,Category
from django.db.models import Q

# Create your views here.

# start post by category
def post_by_category(request,category_id):
    
    
    posts=Blog.objects.filter(category=category_id)
    try:
        category=Category.objects.get(pk=category_id)
    except:
        return redirect('indexpage')
    # category=get_object_or_404(Category,pk=category_id)
    context={
        'posts':posts,
        
    }
    return render(request,'frontend/pages/post_by_category.html',context)
# end

# start python
def python(request):
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True,status='1').order_by('-updated')
    python=Blog.objects.filter(category_id=5)
    
    context={
        'featured_posts':featured_posts,
        'categories':categories,
        'python':python
        }
    return render(request,'frontend/pages/python.html',context) 
# end python

# single blog post
def single_blog_post(request,slug):
    return HttpResponse(slug)
# end single blog post

# serch views
def search(request):
    new_keyword=request.GET.get('keyword')
    search_posts=Blog.objects.filter(Q(title__icontains=new_keyword)|
                                     Q(short_description__icontains=new_keyword))
    context={
        'search_posts':search_posts,
        'new_keyword':new_keyword
        }
    return render(request,'frontend/pages/search.html',context)
# end serch views


