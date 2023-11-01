from django.urls import path
from .views import UserListView, HomeListView, UserDetailView, UserPostsView


urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('users/', UserListView.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:user_id>/posts/', UserPostsView.as_view(), name='user-posts'),
]
