from django.urls import path
from vlog import views 
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('vlist', views.VideoListView.as_view(), name ='vlist'),
    path('video/', views.PostVideoView.as_view(), name ='vlog1'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)