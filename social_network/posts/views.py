from django.shortcuts import render

# Create your views here.
#Публикации могут создаваться только авторизованными пользователями,
# редактировать же публикацию может только её автор.
#ListAPIView, CreateAPIView, RetrieveAPIView,
#UpdateAPIView, DestroyAPIView, and combinations like ListCreateAPIView






#Комментарии могут быть написаны к определённой публикации, оставлять их могут только авторизованные пользователи.
# Сам комментарий состоит из текста и даты его публикации.