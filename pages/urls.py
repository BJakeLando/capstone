from django.urls import path

from .views import (
    AboutView,
    HomeView,
    HelpView,
    LogoutView,
)

urlpatterns= [
    path('about/', AboutView.as_view(), name = 'about'),
    path('home/', HomeView.as_view(), name = 'home'),
    path('help/', HelpView.as_view(), name ='help'),
     path('logout/', LogoutView.as_view(), name ='logout'),
]