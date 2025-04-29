from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Post, Like, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, LikeSerializer, CommentSerializer, CreatePostSerializer, PostDetailsSerializer


# Create your views here.

# to create a new post
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = [IsAuthenticated]


# to get a post by its id, to edit and/or delete a post
class PostDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


# to create a new like
class CreateLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_id = serializer.validated_data['post']
        user_id = request.user
        like_exists = Like.objects.filter(post=post_id, user=user_id).exists()
        if like_exists:
            return Response(status=status.HTTP_409_CONFLICT)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#to delete a like:
class DeleteLikeView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]


#to create a comment
class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#to update a comment
class UpdateCommentView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'pk'
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


#to get a comment by its id
class CommentRetrieveView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'pk'
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


#to delete a comment
class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


# final request
class PostDetailsView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    permission_classes = [IsAuthenticated]
