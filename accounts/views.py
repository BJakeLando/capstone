from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignupView(CreateView):
    template_name= "registration/signup.html"
    success_url = reverse_lazy('login')


