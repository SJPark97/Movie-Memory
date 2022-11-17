from rest_framework import serializers
from .models import Movie, Review, Comment, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class MovieListSerializer(serializers.ModelSerializer):
    genre_id = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(use_url=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user')


class MovieSerializer(serializers.ModelSerializer):
    genre_id = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'
