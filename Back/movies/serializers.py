from rest_framework import serializers
from .models import Movie, Review


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
    # comment_set = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('user', )
