from django import forms
from posts.models import Post


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'name', 'description', 'text', 'status']
        labels = {
            'author': 'Автор',
            'name': 'Название',
            'description': 'Описание',
            'text': 'Содержание',
            'status': 'Статус (Открытый/Закрытый)',
        }
