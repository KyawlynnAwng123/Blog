"""
URL configuration for Base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from Blogs import views  as BlogViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="indexpage"),
    path('category/',include("Blogs.urls")),
    
    # single blog post
    path('single_blog/<slug:slug>/',BlogViews.single_blog_post,name="single_blog_post"),
    
    # search url
    path('blog/search/',BlogViews.search,name='search'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title="Blog Site"
admin.site.site_header="Blog Site Admin"
admin.site.site_title="Blog Site "
