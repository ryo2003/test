from django import forms
from tube_extension.models import Video


        
class DurationForm(forms.Form):
    durations = forms.IntegerField()
    
    