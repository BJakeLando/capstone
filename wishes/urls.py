from django.urls import path 
from wishes import views

urlpatterns = [
    path('', views.BoardView.as_view(), name ='board'),
    path('<int:pk>', views.WishDetailView.as_view(), name='wish_detail'),
    path('new/', views.WishCreateView.as_view(), name='new_wish'),
    path('<int:pk>/edit/', views.WishUpdateView.as_view(), name='edit_wish'),
    path('<int:pk>/delete/', views.WishDeleteView.as_view(), name='delete_wish'),
]