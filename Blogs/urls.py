from django.urls import path
from .import views
urlpatterns = [
    path('post_by_category/<int:category_id>/',views.post_by_category,name="post_by_category"),
    path('category/',views.python,name="python"),
    
    
    
]
