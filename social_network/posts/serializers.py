from rest_framework import serializers

from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']


class PostSerializer(serializers.ModelSerializer):  # PostComment Serializer
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'user', 'location', 'created_at', 'image', 'comments']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['user']


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'location', 'image']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(CreatePostSerializer, self).create(validated_data)

# class PostDetailsSerializer(serializers.Serializer):
#     post =
#     comment_descrbtion = serializers.CharField()
#     total_likes =