from django import forms
from posts.models import Post, Comment


class BaseModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Post
        fields = ['user', 'title', 'content']


class CommentForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Comment
        fields = ['user', 'content']
