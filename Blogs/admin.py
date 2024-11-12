from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','status','is_featured','category']
    list_editable=('is_featured',)
    list_display_links=['category']
    list_filter=('title','status')
    list_max_show_all=100
    search_fields=['title','category__name']

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
