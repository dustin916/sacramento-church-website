from django import forms
from django.forms import ModelForm, SelectDateWidget
from django.forms.fields import DateField
from .models import Event, Sermon


# Create Event Form
class EventForm(ModelForm):
    class Meta:
        model = Event
        
#        fields = "__all__"  # This could work but what if you don't want all fields being shown?
        fields = ('name', 'event_date', 'event_time', 'description') #This way you can list only the fields you want shown (make sure any you are leaving out are not required)
        labels = {
            'name': '',
            'event_date': 'Date:',
            'event_time': 'Time:',
            'description': '',            
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'event_time': forms.DateInput(attrs={'class':'time', 'type': 'time'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'description'}),
        }

# Create Sermon Form
class SermonForm(ModelForm):
    
    class Meta:
        model = Sermon
        
#        fields = "__all__"  # This could work but what if you don't want all fields being shown?
        fields = ('title', 'speaker', 'audio_file', 'date', 'time')
        labels = {
            'title': '',
            'speaker': '',
            'audio_file': 'Sermon Audio',
            'date': 'Date:',
            'time': 'AM or PM'          
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Sermon Title'}),
            'speaker': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Speaker'}),
            'audio_file': forms.FileInput(attrs={'class':'form-control',}),
            'date': forms.TextInput(attrs={'type': 'date'}),
            'time': forms.TextInput(attrs={'placeholder': 'AM or PM'}),
  
        }
