from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse_lazy
from .models import Post, Status 
from .forms import VideoForm
from .models import Video
from django.shortcuts import render



def showvideo(request):
    lastvideo= Video.objects.last()
    videofile= lastvideo.videofile
    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context= {'videofile': videofile,'form': form}
    return render(request, 'home.html', context)

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            status = Status.objects.get(id=1)
            context["post_list"] = Post.objects.filter(
                status=status).order_by("created_on").reverse()
            return context

class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = Status.objects.get(id=2)
        context["post_list"] = Post.objects.filter(
            status=status).filter(author=self.request.user).order_by("created_on").reverse()
        return context


class PostDetailView(LoginRequiredMixin,DetailView):
    template_name = 'posts/detail.html'
    model = Post


class PostNewView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'body', "status",]


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditView(LoginRequiredMixin, UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ['title','subtitle', 'body', "status"]

    def test_func(self):
        post_obj = self.get_object()
        return self.request.user == post_obj.author

class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('list')

    def test_func(self):
        post_obj = self.get_object()
        return self.request.user == post_obj.author
