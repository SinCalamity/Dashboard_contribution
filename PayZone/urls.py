from django.urls import path
from . import views


app_name = 'PayZone'

urlpatterns = [
    path('PayZone/', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]