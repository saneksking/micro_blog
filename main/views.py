from django.http import HttpResponse
from django.shortcuts import render
from main.models import SiteSettings
from posts.models import Post


def index(request):
    settings = SiteSettings.objects.last()
    post_list = Post.objects.filter(status=True)[:10]
    context = {
        'settings': settings,
        'post_list': post_list,
    }
    return render(request, 'main/index.html', context)
