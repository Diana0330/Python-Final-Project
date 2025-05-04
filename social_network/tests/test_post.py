import pytest
from rest_framework import status
from rest_framework.test import APIClient

from posts.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_obj():
    return User.objects.create_user(username='Peter', email='peter_parker@yahoo.com', password='125874')


@pytest.mark.django_db
def test_create_post_unauthorized(api_client):
    """Test creating a post for a user (checks that unauthenticated user cant create a post and get 401 response"""
    response = api_client.post('/posts/create/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_create_post_authorized_user(api_client, user_obj):
    """Test creating a post for an authenticated user"""
    api_client.force_authenticate(user=user_obj)
    data = {"title": "Easter Sunday",
            "description": "Family Time",
            "location": "Europe"}
    response = api_client.post('/posts/create/', data)
    assert response.status_code == status.HTTP_201_CREATED
   
