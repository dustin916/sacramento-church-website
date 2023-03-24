from django.contrib import admin
from .models import Sermon
from django.contrib.auth.models import Group

# Register your models here.

#admin.site.register(Sermon)


# Remove Groups category from Admin page
admin.site.unregister(Group) # singular


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'date', 'time')
    list_filter = ('speaker', 'date')
    ordering = ('-date',)
    search_fields = ('speaker',)

