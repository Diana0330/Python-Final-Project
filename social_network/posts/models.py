from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User who made a post', related_name='post')
    title = models.CharField(max_length=50, verbose_name='Post Title')
    description = models.TextField(max_length=100, verbose_name='Post Content')
    location = models.CharField(max_length=50, verbose_name='Post Location')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Post Image')

    def __str__(self):
        return f'{self.title} {self.description} {self.location}'


# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    def __str__(self):
        return f' {self.created_at}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    description = models.TextField(max_length=100, verbose_name='Comment Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    def __str__(self):
        return f'{self.description} {self.created_at}'
