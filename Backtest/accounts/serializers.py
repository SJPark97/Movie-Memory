from rest_framework import serializers
from .models import Profile, Notice


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user', 'followings')


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
        read_only_fields = ('user', 'review')