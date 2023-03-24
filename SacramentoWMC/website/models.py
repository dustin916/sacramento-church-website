from django.db import models


class Sermon(models.Model):
    title = models.CharField(max_length=200, null=True)
    speaker = models.CharField(max_length=200, null=True)
    audio_file = models.FileField(upload_to='sermons/', blank=True, null=True) # delete blank=True
    date = models.DateField('Date', null=True) 
    time = models.CharField('Time', max_length=4, null=True)
        


    def __str__(self):
        return self.title + ' - ' + self.speaker
    
    # return time input as uppercase (am/pm = AM/PM)
    def save(self, force_insert=False, force_update=False):
        self.time = self.time.upper()
        super(Sermon, self).save(force_insert, force_update)
