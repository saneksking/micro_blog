from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from posts.models import Post, Comment, Grade, Watcher
from posts.forms import CreatePostForm
from smart.get_ip_master import IpMaster


def posts(request):
    post_list = Post.objects.filter(status=True)

    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context = {
        'objects': objects,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    ip = IpMaster.get_ip(request=request)
    watcher = Watcher.objects.filter(ip=ip, post_id=post.id)
    if watcher.exists():
        update_watcher = Watcher.objects.get(ip=ip, post_id=post.id)
        update_watcher.counter += 1
        update_watcher.save()
    else:
        watch = Watcher.objects.create(ip=ip, post_id=post.id, counter=1)
        watch.save()
    comment_list = Comment.objects.filter(post_id=post.id)
    author = request.POST.get('new_author', None)
    new_comment = request.POST.get('new_comment', None)
    if 'btn' in request.POST:
        comment = Comment.objects.create(
            author=author or 'Гость',
            text=new_comment,
            post_id=post.id,
        )
        comment.save()
        return redirect(reverse('posts:post_detail', args=(post.id,)))
    paginator = Paginator(comment_list, 5)
    comment = request.GET.get('page')
    objects = paginator.get_page(comment)
    context = {
        'post': post,
        'objects': objects,
    }
    return render(request, 'posts/post_detail.html', context)


def post_grade_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    ip = IpMaster.get_ip(request=request)
    grade = Grade.objects.filter(post_id=post.id, ip=ip, grade_status=True).exists()
    if grade:
        return redirect(reverse('posts:post_detail', args=(post.id,)))
    else:
        create_grade = Grade.objects.create(
            post_id=post.id,
            grade_status=True,
            ip=ip,
        )
        create_grade.save()
        return redirect(reverse('posts:post_detail', args=(post.id,)))


def post_grade_dislike(request, post_id):
    post_id = get_object_or_404(Post, id=post_id)
    ip = IpMaster.get_ip(request=request)
    grade = Grade.objects.filter(post_id=post_id.id, ip=ip, grade_status=False).exists()
    if grade:
        return redirect(reverse('posts:post_detail', args=(post_id.id,)))
    else:
        create_grade = Grade.objects.create(
            post_id=post_id.id,
            grade_status=False,
            ip=ip,
        )
        create_grade.save()
        return redirect(reverse('posts:post_detail', args=(post_id.id,)))


def post_create(request):
    form = CreatePostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('posts:posts'))
    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)


def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CreatePostForm(request.POST, instance=post.id)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('posts:posts'))
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/post_update.html', context)


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:posts')


def comment_delete(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(reverse('posts:post_detail', args=(post.id,)))
