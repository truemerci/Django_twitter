from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from users.models import CustomUser
from posts.models import Post


class HomeListView(ListView):
    model = CustomUser
    template_name = 'users/home.html'
    context_object_name = 'users'


class UserListView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user)
        return context


class UserPostsView(ListView):
    model = Post
    template_name = 'users/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(CustomUser, pk=self.kwargs['user_id'])
        posts = Post.objects.filter(user=user)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(CustomUser, pk=self.kwargs['user_id'])
        return context
