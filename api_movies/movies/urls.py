from . import views
from django.urls import path, include

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movie/<int:pk>/', views.MovieDetail.as_view()),
    
]