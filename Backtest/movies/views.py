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
from .models import Movie, Review, Comment


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
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
    # review = Review.objects.get(pk=review_pk)
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
    # movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
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
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
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
        # review = Review.objects.get(pk=review_pk)
        review = get_object_or_404(Review, pk=review_pk)
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


@api_view(['POST', 'GET'])
def like_movies(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소 (remove)
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가 (add)
        movie.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'like_users_count': movie.like_users.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['POST'])
def like_reviews(request, movie_pk):
    review = get_object_or_404(Review, pk=movie_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소 (remove)
        review.like_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가 (add)
        review.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'like_users_count': review.like_users.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['POST'])
def like_comments(request, movie_pk):
    comment = get_object_or_404(Comment, pk=movie_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소 (remove)
        comment.like_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가 (add)
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
    movies = movies.order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)