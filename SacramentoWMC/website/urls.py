from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('faith/', views.faith, name='faith'),
    path('sermons/', views.sermon_list, name='sermon-list'),
    path('add-sermon/', views.add_sermon, name='add-sermon'),
    path('delete-sermon/<sermon_id>', views.delete_sermon, name='delete-sermon'),
    path('sermon/<sermon_id>', views.sermon, name='sermon'),
    path('search-sermons/', views.search_sermons, name='search-sermons'),  
    path('contact/', views.contact, name='contact'),
]
