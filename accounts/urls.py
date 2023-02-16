from django.urls import path
from .views import (SignupView,
                    profileHome,
                    profile_list,
                    profile)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profiles/', profile_list, name='profiles'),
    path('profileHome/', profileHome, name='profileHome'),
    path('profile/<int:pk>/', profile, name = 'myProfile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)