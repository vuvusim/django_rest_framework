from . import views
from django.urls import path, include

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movie/<int:pk>/', views.MovieDetail.as_view()),

    path('movie/<int:pk>/reviews', views.ReviewList.as_view()),
    
    path('review/<int:pk>/', views.ReviewDetail.as_view()),
    path('movie/<int:pk>/like/', views.MovieLikeCreate.as_view()),
]