from django.urls import path
from . import views

urlpatterns = [
    path('login_manager', views.login_manager, name='login'),
    path('logout_manager', views.logout_manager, name='logout'),
    path('register_manager', views.register_manager, name='register'),
    
]