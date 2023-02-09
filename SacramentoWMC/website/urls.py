from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sermons/', views.sermon_list, name='sermon-list'),
    path('add-sermon/', views.add_sermon, name='add-sermon'),
    path('delete-sermon/<sermon_id>', views.delete_sermon, name='delete-sermon'),
    path('sermon/<sermon_id>', views.sermon, name='sermon'),
    path('search-sermons/', views.search_sermons, name='search-sermons'),  
    path('calendar/', views.calndr, name='calendar'),
    path('<int:year>/<str:month>/', views.calndr, name='calendar'), 
    path('events/', views.event_list, name='event-list'), 
    path('add-event/', views.add_event, name='add-event'),
    path('update-event/<event_id>', views.update_event, name='update-event'),
    path('delete-event/<event_id>', views.delete_event, name='delete-event'),
    path('contact/', views.contact, name='contact'),
]
