from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

# Authentication Decorators
# from rest_framework.decorators import authentication_classes
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer
from .models import Profile

# Create your views here.
@api_view(['GET', 'PUT', 'POST'])
def my_profile(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        profile = get_object_or_404(Profile, user=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def user_profile(request, user_id):
    profile = get_object_or_404(Profile, user=user_id)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, user_id):
    person = get_object_or_404(get_user_model(), pk=user_id)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            is_followed = False
        else:
            person.followers.add(user)
            is_followed = True
        context = {
            'is_followed': is_followed,
            'followers_count': person.followers.count(),
            'followings_count': person.followings.count(),
        }
        return Response(context, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_202_ACCEPTED)
