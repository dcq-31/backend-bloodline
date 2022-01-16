from django.urls import path
from .views import DogList, DogDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('dogs/', DogList.as_view()),
  path('dogs/<int:pk>/', DogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)