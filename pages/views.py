from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='pages/home.html'

class AboutView(TemplateView):
    template_name='pages/about.html'

class HelpView(TemplateView):
    template_name ='pages/help.html'
    
class LogoutView(TemplateView):
    template_name ='registration/logged_out.html'

