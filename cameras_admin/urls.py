from django.urls import path
from cameras_admin import views

urlpatterns = [
    path('', views.cameras, name='cameras'),
    path('created/', views.create_camera, name='create_camera'),
    path('<id>/', views.edit_camera, name='edit_camera'),
    path('delete/<id>/', views.delete_camera, name='delete_camera'),
    path('rtsp/<id>/', views.rtsp_camera, name='rtsp_camera'),
]
