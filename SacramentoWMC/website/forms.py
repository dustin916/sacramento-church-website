from django import forms
from django.forms import ModelForm
from .models import  Sermon

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


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

class ContactForm(forms.Form):
    subject = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Subject',
        'name': 'subject',
        }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Name',
        'name': 'name',
        
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'email@example.com',
        'name': 'email',
        
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        "rows":"5",
        'placeholder':'Type your message here.',
        'name': 'message',
        
        }))
    captcha = ReCaptchaField(required=True, widget=ReCaptchaV2Checkbox(
        attrs={
            "class":"g-recaptcha"
        }
    )) 

