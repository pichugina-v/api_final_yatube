from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    def validate(self, attrs):
        user = self.context['request'].user
        following = attrs['following']
        if user == following:
            raise ValidationError('Вы не можете подписаться на самого себя')
        if Follow.objects.filter(
            user=user,
            following=following
        ).exists():
            raise ValidationError('Подписка уже существует')
        return attrs

    class Meta:
        fields = '__all__'
        model = Follow
