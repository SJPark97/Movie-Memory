from rest_framework import serializers
from .models import Movie, Review, Comment


class MovieListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('id', 'title', 'content')
        # fields = ('id', 'title', 'content', 'user', 'username')


class ReviewSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(use_url=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    # review_set = CommentSerializer(many=True, read_only=True)
    # review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('user', )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)