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
    reviews_count = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)

    def get_reviews_count(self, obj):
        return models.Review.objects.filter(movie=obj).count()


    class Meta:
        model = models.Movie
        fields = ('id', 'title', 'description', 'genre', 'movie_length', 'created_at', 'user', 'user_id', 'reviews_count', 'reviews')

