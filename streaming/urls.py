from django.contrib import admin
from django.urls import path, include
from dashboard import views as dash_views
from cameras_admin.views import video_feed
from members.views import login

urlpatterns = [
    path('', login, name='login'),
    path('dashboard/', dash_views.index, name="dashboard"),
    
    path('cameras/', include('cameras_admin.urls')),
    path('video_feed/', video_feed, name='video_feed'),
    
    path('members/', include('members.urls')),
    
    path('plates/', include('plates.urls')),
    
    path('admin/', admin.site.urls),
]
