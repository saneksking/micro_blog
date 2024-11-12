from django import template
from posts.models import Grade, Post, Comment, Watcher

register = template.Library()


@register.simple_tag
def post_grade_like(post_id):
    return Grade.objects.filter(post_id=post_id, grade_status=True).count()


@register.simple_tag
def post_grade_dislike(post_id):
    return Grade.objects.filter(post_id=post_id, grade_status=False).count()


@register.simple_tag
def post_count():
    return Post.objects.all().count()


@register.simple_tag
def comment_count(post_id):
    return Comment.objects.filter(post_id=post_id).count()


@register.simple_tag
def unique_watch(post_id):
    return Watcher.objects.filter(post_id=post_id).count()


@register.simple_tag
def watch(post_id):
    list_watcher = Watcher.objects.filter(post_id=post_id).values_list('counter', flat=True)
    return sum(list_watcher)


