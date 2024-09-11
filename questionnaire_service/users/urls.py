
from django.urls import path
from .views import UserCreateView, ProfileDetailView, ThreadListCreateView, ThreadDetailView, ResponseListCreateView, ResponseDetailView
# urls here:

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('threads/', ThreadListCreateView.as_view(), name='thread-list-create'),
    path('threads/<int:pk>/', ThreadDetailView.as_view(), name='thread-detail'),
    path('responses/', ResponseListCreateView.as_view(), name='response-list-create'),
    path('responses/<int:pk>/', ResponseDetailView.as_view(), name='response-detail'),
]

