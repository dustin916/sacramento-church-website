from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sermons/', views.sermons, name='sermons'),  
    #path('calendar/', views.calendar, name='calendar'),
    path('<int:year>/<str:month>/', views.calendar, name='calendar'),  
    path('contact/', views.contact, name='contact'),
]
