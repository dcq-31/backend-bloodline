from django.urls import path
from bloodline_api.views.dog import DogDetail, DogList
from bloodline_api.views.user import UserDetail, UserList
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

urlpatterns = [
  path('users/', UserList.as_view()),
  path('users/<int:pk>/', UserDetail.as_view()),
  path('dogs/', DogList.as_view()),
  path('dogs/<int:pk>/', DogDetail.as_view()),
  # Get auth token
  path('login/', views.obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)