from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from django.urls import reverse_lazy

from tube_extension.models import Video
from tube_extension.forms import DurationForm




class VideoFormView(CreateView):
    template_name = "tube_extension/video_list.html"
    model=Video
    fields = ['title','link']
    success_url = "/"
    

    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['videos'] = Video.objects.filter(user=self.request.user)
        return ctx
        
     
    def form_valid(self,form):   
        video = form.save()
        print(video.id)
        video.title = self.request.POST.get('title')
        link = self.request.POST.get('link')
        video.link = link.split("v=")[1].split("&")[0]
        video.user = self.request.user
        #print(video_id)
        #video.save()
        return super().form_valid(form)
    
class WatchVideoView(FormView):
    form_class=DurationForm
    template_name = "tube_extension/video_detail.html"
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['object'] = Video.objects.get(id=self.kwargs['pk'])
        return ctx
        
    def form_valid(self,form):
        print("成功")
        return super().form_valid(form);
    


    
    
