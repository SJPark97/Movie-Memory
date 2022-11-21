from rest_framework.response import Response
from rest_framework.decorators import api_view

# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import (
    MovieListSerializer,
    MovieSerializer,
    ReviewSerializer,
    CommentSerializer,
    ReviewListSerializer,
)
from accounts.serializers import NoticeSerializer
from .models import Movie, Review, Comment
# from accounts.serializers import ProfileSerializer
from accounts.models import Profile

all_genres = {
    28: 'action',
    12: 'adventure',
    16: 'animation',
    35: 'comedy',
    80: 'crime',
    99: 'documentary',
    18: 'drama',
    10751: 'family',
    14: 'fantasy',
    36: 'history',
    27: 'horror',
    10402: 'music',
    9648: 'mystery',
    10749: 'romance',
    878: 'science',
    10770: 'tv',
    53: 'thriller',
    10752: 'war',
    37: 'western',
    }

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    movies = get_list_or_404(Movie)
    movies = movies[:400]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_create(request, movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        genres = movie.genres.all()
        profile = get_object_or_404(Profile, user=request.user.id)
        for i in range(len(genres)):
            g = all_genres.get(genres[i].id)
            if g == 'action':profile.action += 1
            elif g == 'adventure':profile.adventure += 1
            elif g == 'animation':profile.animation += 1
            elif g == 'comedy':profile.comedy += 1
            elif g == 'crime':profile.crime += 1
            elif g == 'documentary':profile.documentary += 1
            elif g == 'drama':profile.drama += 1
            elif g == 'family':profile.family += 1
            elif g == 'fantasy':profile.fantasy += 1
            elif g == 'history':profile.history += 1
            elif g == 'horror':profile.horror += 1
            elif g == 'music':profile.music += 1
            elif g == 'mystery':profile.mystery += 1
            elif g == 'romance':profile.romance += 1
            elif g == 'science':profile.science += 1
            elif g == 'tv':profile.tv += 1
            elif g == 'thriller':profile.thriller += 1
            elif g == 'war':profile.war += 1
            elif g == 'western':profile.western += 1
        profile.save()

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        reviews = get_list_or_404(Review, movie=movie_pk)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment_create(request, review_pk):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk=review_pk)
        if request.user != review.user:
            serializer = NoticeSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(review=review, user=review.user, content=review.title + '에 댓글이 달렸습니다.')
                return Response(status=status.HTTP_201_CREATED)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = get_list_or_404(Comment, review=review_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def user_reviews(request, user_pk):
    reviews = get_list_or_404(Review, user=user_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_comments(request, user_pk):
    comments = get_list_or_404(Comment, user=user_pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def like_movies(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        movie.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'like_users_count': movie.like_users.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['POST'])
def like_reviews(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'like_users_count': review.like_users.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['POST'])
def like_comments(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
        is_liked = False
    else:
        comment.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'like_users_count': comment.like_users.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def genres_movies(request, genres_pk):
    movies = Movie.objects.filter(genres = genres_pk)
    movies = movies.order_by('-popularity')[:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def like_movies(request, user_pk):
    movies = Movie.objects.filter(like_users = user_pk)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def like_reviews(request, user_pk):
    reviews = Review.objects.filter(like_users = user_pk)
    reviews = reviews.order_by('-created_at')
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)