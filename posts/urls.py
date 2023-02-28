from django.urls import path
from posts import views 

urlpatterns = [
    path('', views.PostListView.as_view(), name ='list'),
    path('drafts/', views.DraftPostListView.as_view(), name ='drafts'),
    path('<int:pk>/', views.PostDetailView.as_view(), name ='detail'),
    path('new/', views.PostNewView.as_view(), name ='new'),
    path('edit/<int:pk>/', views.PostEditView.as_view(), name = 'edit'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name ='delete'),
] 