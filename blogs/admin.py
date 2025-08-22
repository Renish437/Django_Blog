from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','created_at','updated_at')

class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','slug','category','author','blog_image','status','is_featured','is_popular','is_trending','created_at','updated_at')
    prepopulated_fields={'slug':('title',)}
    search_fields = ('title','category__category_name','status')
    list_editable = ('is_featured','is_popular','is_trending','status')
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
