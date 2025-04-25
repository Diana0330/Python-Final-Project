from django.urls import path

from .views import PostDetailsUpdateDeleteView, CreateLikeView, DeleteLikeView, CreateCommentView, \
    UpdateCommentView, CommentRetrieveView, CommentDeleteView, PostCreateView

urlpatterns = [
    path('posts/create/', PostCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailsUpdateDeleteView.as_view()),
    path('likes/create/', CreateLikeView.as_view()),
    path('likes/<int:pk>/', DeleteLikeView.as_view()),
    path('comments/create/', CreateCommentView.as_view()),
    path('comments/update/<int:pk>/', UpdateCommentView.as_view()),
    path('comments/<int:pk>/', CommentRetrieveView.as_view()),
    path('comments/delete/<int:pk>/', CommentDeleteView.as_view()),


]