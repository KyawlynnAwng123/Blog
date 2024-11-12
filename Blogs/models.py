from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# start category model
class Category(models.Model):
    name = models.CharField(max_length = 200,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural="Categories"
    
    def __str__(self):
        return self.name
    
# end category model

STATUS_CHOICES = (
        (0,"Draft"),
        (1, "Plushied")
)

# start blog model
class Blog(models.Model):
    title = models.CharField(max_length =100)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    auther=models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='images/%Y/%m/%d')
    short_description=models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status=models.IntegerField(choices=STATUS_CHOICES)
    is_featured=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
    

    
    
# end blog model