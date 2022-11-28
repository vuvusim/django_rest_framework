from django.shortcuts import render
from . import serializers, models
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
            raise ValidationError('You can not edit other users movie')
        