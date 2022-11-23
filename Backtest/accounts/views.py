from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

# Authentication Decorators
# from rest_framework.decorators import authentication_classes
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer, NoticeSerializer
from .models import Profile, Notice
from movies.models import Review

# Create your views here.
@api_view(['GET', 'PUT', 'POST'])
def my_profile(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        profile = Profile.objects.get(user=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        profile = Profile.objects.get(user=request.user.id)
        profile.delete()
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


@api_view(['GET'])
def user_profile(request, user_id):
    profile = Profile.objects.get(user=user_id)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def follow(request, user_id):
    person = get_user_model().objects.get(pk=user_id)
    user = request.user
    if request.method == 'POST':
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
    elif request.method == 'GET':
        if person.followers.filter(pk=user.pk).exists():
            is_followed = True
        else:
            is_followed = False
        context = {
            'is_followed': is_followed,
            'followers_count': person.followers.count(),
            'followings_count': person.followings.count(),
        }
        return Response(context, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def genres_movies(request):
    profile = Profile.objects.get(user=request.user.id)
    genres = {
    28: profile.action,
    12: profile.adventure,
    16: profile.animation,
    35: profile.comedy,
    80: profile.crime,
    99: profile.documentary,
    18: profile.drama,
    10751: profile.family,
    14: profile.fantasy,
    36: profile.history,
    27: profile.horror,
    10402: profile.music,
    9648: profile.mystery,
    10749: profile.romance,
    878: profile.science,
    10770: profile.tv,
    53: profile.thriller,
    10752: profile.war,
    37: profile.western,
    }
    best_genre = sorted(genres.items(), key=lambda x: -x[1])[0][0]
    return redirect('movies:genre_recommend', best_genre)


@api_view(['GET'])
def my_notice(request):
    notices = Notice.objects.filter(user = request.user)
    notices = notices.order_by('-id')
    serializer = NoticeSerializer(notices, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def change_notice(request, notice_id):
    notice = Notice.objects.get(id = notice_id)
    notice.is_checked = True
    notice.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def new_kind_movies(request):
    profile = Profile.objects.get(user=request.user.id)
    genres = {
    28: profile.action,
    12: profile.adventure,
    16: profile.animation,
    35: profile.comedy,
    80: profile.crime,
    99: profile.documentary,
    18: profile.drama,
    10751: profile.family,
    14: profile.fantasy,
    36: profile.history,
    27: profile.horror,
    10402: profile.music,
    9648: profile.mystery,
    10749: profile.romance,
    878: profile.science,
    10770: profile.tv,
    53: profile.thriller,
    10752: profile.war,
    37: profile.western,
    }
    new_genre = sorted(genres.items(), key=lambda x: x[1])[0][0]
    return redirect('movies:genre_recommend', new_genre)


@api_view(['DELETE'])
def delete_checked_notice(request):
    notices = Notice.objects.filter(user = request.user, is_checked = True)
    notices.delete()
    return Response(status=status.HTTP_200_OK)