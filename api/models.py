from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return (f'Текст поста: {self.text[:15]}, '
                f'дата публикации: {self.pub_date}, '
                f'автор поста: {self.author.username}, '
                f'группа: {self.group}')


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return (f'Автор комментария: {self.author.username}, '
                f'текст комментария: {self.text[:15]}, '
                f'к посту: {self.post.text[:15]}, '
                f'дата добавления: {self.created}')


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    def __str__(self):
        return (f'Подписчик: {self.user.username}, '
                f'подписан на: {self.following.username} ')
