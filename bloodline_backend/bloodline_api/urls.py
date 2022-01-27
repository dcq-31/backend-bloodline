from django.urls import path
from .views import UserDetail, UserList, DogDetail, DogList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('users/', UserList.as_view()),
  path('users/<int:pk>/', UserDetail.as_view()),
   path('dogs/', DogList.as_view()),
  path('dogs/<int:pk>/', DogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)