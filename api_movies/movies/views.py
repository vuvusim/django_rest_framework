from django.shortcuts import render
from . import serializers, models
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response



class MovieList(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        movie = models.Movie.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if movie.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_('You can not delete other users movie.'))

    def put(self, request, *args, **kwargs):
        movie = models.Movie.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if movie.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_('You can not edit other users movie'))
        

class ReviewList(generics.ListCreateAPIView):
    # queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        movie = models.Movie.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, movie=movie)

    def get_queryset(self):
        movie = models.Movie.objects.get(pk=self.kwargs['pk'])
        return models.Review.objects.filter(movie=movie)



class ReviewDetail(generics.RetrieveUpdateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        review = models.Review.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if review.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_('You can not delete other users reviews'))

    def put(self, request, *args, **kwargs):
        review = models.Review.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if review.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_('You can not change other users reviews'))


class MovieLikeCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = serializers.MovieLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        movie = models.Movie.objects.get(pk=self.kwargs['pk'])
        return models.MovieLike.objects.filter(user=user, movie=movie)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError(_('You can not like the post more than once'))
        user = self.request.user
        movie = models.Movie.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=user, movie=movie)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError(_('You do not like this post to begin with'))