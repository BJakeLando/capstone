from django.urls import path
from .views import (SignupView,
                    profileHome,
                    profile_list,
                    profile)

urlpatterns= [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profiles/', profile_list, name='profiles'),
    path('profileHome/', profileHome, name='profileHome'),
    path('profile/<int:pk>/', profile, name = 'myProfile'),
]