from rest_framework import serializers
from . import models

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    movie = serializers.ReadOnlyField(source='movie.id')

    class Meta:
        model = models.Review
        fields = ('id', 'movie', 'body', 'created_at', 'user', 'user_id')

        
class MovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = models.Movie
        fields = ('id', 'title', 'description', 'genre', 'movie_length', 'created_at', 'user', 'user_id', 'reviews')

