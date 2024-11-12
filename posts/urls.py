from posts import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('like/<int:post_id>/', views.post_grade_like, name='grade_like'),
    path('dislike/<int:post_id>/', views.post_grade_dislike, name='grade_dislike'),
    path('post-create/', views.post_create, name='post_create'),
    path('post-update/<int:post_id>/', views.post_update, name='post_update'),
    path('post-delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('post/<int:post_id>/comment-delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
