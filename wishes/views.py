from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Wish
from django.urls import reverse_lazy


class BoardView(ListView):
    template_name ="wishes/board.html"
    model = Wish

class WishDetailView(LoginRequiredMixin, DetailView):
    template_name = "wishes/detail.html"
    model = Wish

class WishCreateView(CreateView):
    template_name = "wishes/new.html"
    model = Wish
    fields = ['summary', 'description', 'assignee']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WishUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "wishes/edit.html"
    model = Wish
    fields = ['summary', 'description', 'assignee']

    def test_func(self):
        wish_obj = self.get_object()
        return self.request.user == wish_obj.author

class WishDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "wishes/delete.html"
    model = Wish
    success_url = reverse_lazy('board')

    def test_func(self):
        wish_obj = self.get_object()
        return self.request.user == wish_obj.author

class SuccessView(TemplateView):
    template_name = "wishes/success.html" 
    model = Wish


