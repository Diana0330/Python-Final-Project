from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Post, Like, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, LikeSerializer, CommentSerializer, CreatePostSerializer


# Create your views here.
#Публикации могут создаваться только авторизованными пользователями,
# редактировать же публикацию может только её автор.


# to create a new post and to retrieve all posts

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
class CreateLikeView(
    generics.CreateAPIView):  # one user can make many likes, before doing a post - is there a like for a certain post
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    # def post/create method or composite primary key???

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#to delete a like:
class DeleteLikeView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]


#Комментарии могут быть написаны к определённой публикации, оставлять их могут только авторизованные пользователи.
# Сам комментарий состоит из текста и даты его публикации.
class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateCommentView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'pk'
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CommentRetrieveView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'pk'
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]