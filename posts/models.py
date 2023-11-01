from django.db import models
from django.urls import reverse
from users.models import BaseModel


class Post(BaseModel):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField(blank=False)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user}: {self.title}'


class Comment(BaseModel):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(blank=False)

    def __str__(self):
        return f'{self.user}: {self.id}'
