
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Profile, Thread, Response
from .serializers import UserSerializer, ProfileSerializer, ThreadSerializer, ResponseSerializer
from rest_framework.permissions import IsAuthenticated
# views here.


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class ThreadListCreateView(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ThreadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]


# Add authentication to ResponseListCreateView and ResponseDetailView
class ResponseListCreateView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]  # Added authentication


class ResponseDetailView(generics.RetrieveAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]  # Added authentication


# Handle missing or invalid slug in ThreadResponseView
class ThreadResponseView(generics.ListAPIView):
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        thread_slug = self.kwargs.get('slug')
        if not thread_slug:
            return Response.objects.none()  # Return empty queryset if slug is missing
        return Response.objects.filter(thread__slug=thread_slug, thread__user=self.request.user)

