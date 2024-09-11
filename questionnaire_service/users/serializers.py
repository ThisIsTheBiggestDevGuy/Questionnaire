
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Thread, Response

# serializers here:


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user']


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'user', 'title', 'description', 'question', 'is_public']


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'thread', 'question', 'answer_text', 'selected_options', 'submitted_at']

