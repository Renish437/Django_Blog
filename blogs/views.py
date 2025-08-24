from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def post_by_category(request, category_id):
    # Logic to fetch and display posts by category
    
    blogs = Blog.objects.filter(category=category_id, status='published').order_by('-created_at')
    
    category = get_object_or_404(Category, id=category_id)
   
    popular_blogs = Blog.objects.filter(status='published' ,is_popular=True).order_by('-created_at')[:5]

    context = {
        'blogs': blogs,
        'category': category,
        
        'popular_blogs': popular_blogs,
    }
    
    return render(request, 'post_category.html',context)
def post_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    recent_blogs = Blog.objects.filter(status='published' ,is_featured=True).order_by('-created_at')[:5]
    context = {
        'blog': blog,
     
        'recent_blogs': recent_blogs
    }
    return render(request, 'post_details.html', context)