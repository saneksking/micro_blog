from posts.models import Grade, Post, Comment, Watcher


def post_grade_like(request, post_id):
    return {'post_grade': Grade.objects.filter(post_id=post_id).count()}


def post_grade_dislike(request, post_id):
    return Grade.objects.filter(post_id=post_id, grade_status=False).count()


def post_count(request):
    return {'post_count': Post.objects.all().count()}


def comment_count(request, post_id):
    return {'comment_count': Comment.objects.filter(post_id=post_id).count()}


def unique_watch(request, post_id):
    return {'unique_watch': Watcher.objects.filter(post_id=post_id).count()}


def watch(request, post_id):
    list_watcher = Watcher.objects.filter(post_id=post_id).values_list('counter', flat=True)
    return {'watch': sum(list_watcher)}


