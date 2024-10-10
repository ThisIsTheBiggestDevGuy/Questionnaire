
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Thread, Response
from ..questionnaire.serializers import QuestionSerializer, OptionSerializer

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
    url = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = ['id', 'user', 'title',
                  'description', 'question',
                  'is_public', 'url']
    def get_url(self, obj):
        return obj.get_absolute_url()


class ResponseSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    selected_opstions = OptionSerializer(many=True)

    def get_queryset(self):
        return Response.objects.filter(thread_user=self.request.user)
    class Meta:
        model = Response
        fields = ['id', 'thread', 'question', 'answer_text', 'selected_options', 'submitted_at']

