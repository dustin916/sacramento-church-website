from django.contrib import admin
from .models import Manager, Sermon, Event, Subscriber
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Manager)
#admin.site.register(Sermon)
#admin.site.register(Event)
admin.site.register(Subscriber)

# Remove Groups category from Admin page
admin.site.unregister(Group) # singular


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'date', 'time')
    list_filter = ('speaker', 'date')
    ordering = ('-date',)
    search_fields = ('speaker',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'event_date', 'description', 'manager') # if you want to put things together (on same row) use, for example, (('name', 'event_date'), description)
    #fields is the page where we can add things. list_display is the main page.
    list_display = ('name', 'event_date')
    list_filter = ('event_date',)
    ordering = ('event_date',)
    search_fields = ('name', 'description')
    