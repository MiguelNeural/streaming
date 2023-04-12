"""streaming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from dashboard import views as dash_views
from cameras_admin import views as cam_views

urlpatterns = [
    path('', dash_views.blank, name='blank'),
    path('dashboard/', dash_views.index, name="dashboard"),
    
    path('cameras/', cam_views.cameras, name='cameras'),
    path('cameras/created/', cam_views.create_camera, name='create_camera'),
    path('cameras/<id>/', cam_views.edit_camera, name='edit_camera'),
    path('cameras/delete/<id>/', cam_views.delete_camera, name='delete_camera'),
    path('cameras/rtsp/<id>', cam_views.rtsp_camera, name='rtsp_camera'),
    
    path('video_feed/', cam_views.video_feed, name='video_feed'),
    
    path('admin/', admin.site.urls),
]
