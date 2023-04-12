from django.urls import path
from members import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', views.members, name='members'),
    
]
