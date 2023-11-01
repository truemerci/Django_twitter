from django.urls import path
from .views import CommentListView, PostDetailView, PostCreateView, PostListView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('add-post/<int:user_id>/', PostCreateView.as_view(), name='add-post'),
    path('<int:post_id>/add-comment/', CommentCreateView.as_view(), name='add-comment'),
]
