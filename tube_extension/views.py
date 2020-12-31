from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from tube_extension.models import Video
from tube_extension.forms import VideoForm


class VideoFormView(FormView):
    template_name = "tube_extension/video_list.html"
    form_class = VideoForm
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['videos'] = Video.objects.filter(user=self.request.user)
        return ctx
    
    def form_valid(self,form):
        form.save(self.request)
        return super().form_valid(form)
    
class WatchVideoView(DetailView):
    model = Video