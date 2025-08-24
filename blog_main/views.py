
from django.shortcuts import render
from blogs.models import *
def home(request):
    featured_blogs = Blog.objects.filter(status='published' ,is_featured=True).order_by('created_at')
    recent_blogs = Blog.objects.filter(status='published' ,is_featured=True).order_by('-created_at')
    trending_blogs = Blog.objects.filter(status='published' ,is_trending=True).order_by('-created_at')[:4]
    popular_blogs = Blog.objects.filter(status='published' ,is_popular=True).order_by('-created_at')
  
    context ={
       
        'featured_blogs':featured_blogs,
        'recent_blogs':recent_blogs,
        'trending_blogs':trending_blogs,
        'popular_blogs':popular_blogs
    }
    return render(request,'home.html',context)
