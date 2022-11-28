from rest_framework import serializers
from . import models

class MovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = models.Movie
        fields = ('id', 'title', 'description', 'genre', 'movie_length', 'created_at', 'user', 'user_id')