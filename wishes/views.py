from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class WishUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    template_name = "wishes/edit.html"
    model = Wish
    fields = ['summary', 'description', 'assignee']

    def test_fun(self):
        wish_obj = self.get_object()
        return self.request.reporter == wish_obj.user

class WishDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "wishes/delete.html"
    model = Wish
    success_url = reverse_lazy('board')

    def test_fun(self, pk):
        wish_obj = self.get_object(pk)
        wish_obj.delete()
        return self.request.reporter == wish_obj.user
