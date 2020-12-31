from django import forms
from tube_extension.models import Video

class VideoForm(forms.Form):
    title = forms.CharField()
    link = forms.CharField()
    
    def save(self,request):
        data=self.cleaned_data
        video_id = data['link'].split("v=")[1].split("&")[0]
        video = Video(title=data['title'],link=video_id)
        video.user = request.user
        video.save()