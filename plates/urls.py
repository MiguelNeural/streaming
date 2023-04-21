from django.urls import path
from plates import views

urlpatterns = [
    path('', views.plates, name='plates'),
]
