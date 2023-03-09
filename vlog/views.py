
from django.views.generic.edit import CreateView

from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Video
from .forms import VideoForm
from django.shortcuts import render



class VideoListView(ListView):
    template_name = 'vlog/vlist.html'
    model = Video

    def showvideo(request):
        form= VideoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        context= {'lastvideo': Video.objects.all().order_by("-created_on"),
                'form': form
                }
        return render(request, 'vlog/vlist.html', context)

class PostVideoView(CreateView):
    template_name = 'vlog/video.html'
    model = Video 
    fields = ['name', 'videofile', 'author', 'description']
    success_url = reverse_lazy('vlist')

    def videoPost(self, request):
        form = VideoForm(request.POST, request.FILES)

        context = {
            'form': form
        }
        if form.is_valid():
            form.save()

        return render(request, 'vlog/vlist.html', context)
