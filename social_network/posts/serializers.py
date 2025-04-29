from rest_framework import serializers

from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']


class PostSerializer(serializers.ModelSerializer):  # PostComment Serializer
    #comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'user', 'location', 'created_at', 'image']


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


class CommentDetailsSerializer(serializers.ModelSerializer):
    text = serializers.CharField(source='description')
    author = serializers.IntegerField(source='user.id')

    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']


class PostDetailsSerializer(serializers.ModelSerializer):
    comments = CommentDetailsSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField('get_total_likes')
    text = serializers.CharField(source='title')

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'created_at', 'comments', 'likes_count']
        read_only_fields = ['likes_count']

    def get_total_likes(self, obj):
        likes_count = obj.like.count()
        return likes_count
