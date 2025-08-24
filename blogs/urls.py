from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   
    path('category/<int:category_id>/',views.post_by_category,name="post_by_category"),
    path('<str:slug>/',views.post_details,name="post_details"),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
