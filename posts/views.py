from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = Comment.objects.filter(post=post)
        return context


class CommentListView(ListView):
    model = Comment
    template_name = 'posts/comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        comments = Comment.objects.filter(post=post)
        return comments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return context


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'posts/create_post.html'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/create_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return context

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('comment-list', args=[self.kwargs['post_id']])
