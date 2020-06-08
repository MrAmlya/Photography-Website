from django.urls import path
from . import views

from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name="post_new"),
    path('path/<int:pk>/edit/', views.post_edit, name="post_edit"),
    path('path/<int:pk>/remove/', views.post_remove, name="post_remove"),
    path('signup/', views.signup, name="signup"),
    path('image_upload/', hotel_image_view, name = 'image_upload'), 
    path('success', success, name = 'success'), 
    path('image_list/', display_hotel_images, name = 'image_list'),
    
]


if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)