from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание')
    text = models.TextField(default='', verbose_name='Текст')
    status = models.BooleanField(default=False, verbose_name='Статус публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.text[:300]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField(default='', verbose_name='Комментарий')
    author = models.CharField(max_length=50, verbose_name='Автор', default='Гость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.text


class Grade(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='grade')
    grade_status = models.BooleanField(null=True)
    ip = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class Watcher(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='watcher')
    ip = models.CharField(max_length=50)
    counter = models.PositiveIntegerField(default=0)

