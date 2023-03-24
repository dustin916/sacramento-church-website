from django import forms
from django.forms import ModelForm
from .models import  Sermon


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
