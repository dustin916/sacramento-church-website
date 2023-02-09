from django.db import models
from django.contrib.auth.models import User #the django user authentication system (logs us in to the admin area)
from datetime import date

class Manager(models.Model):
    first_name = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    email = models.EmailField('Email Address', blank=True)

    #passwords

    def __str__(self):
        return self.first_name + ' ' + self.last_name 


class Sermon(models.Model):
    title = models.CharField(max_length=200, null=True)
    speaker = models.CharField(max_length=200, null=True)
    audio_file = models.FileField(upload_to='sermons/', blank=True, null=True) # delete blank=True
    date = models.DateField('Date', null=True) 
    time = models.CharField('Time', max_length=4, null=True)
        


    def __str__(self):
        return self.title + ' - ' + self.speaker

    
class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateField('Event Date', null=True)
    event_time = models.TimeField('Event Time', null=True)
    description = models.TextField(blank=True) # blank=True means you do not have to have a description.
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name 

        #this allows us to use our model in the admin section

    @property
    def Days_til(self):
        today = date.today()
        days_til = self.event_date - today
        days_til_stripped = str(days_til).split(",", 1)[0]

        if self.event_date < today:
            thing = 'Past'
        else:
            thing = days_til_stripped
        return thing

class Subscriber(models.Model):
    first_name = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    email = models.EmailField('Email Address', blank=True)
    phone = models.CharField('Phone Number', max_length=15, blank=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name 