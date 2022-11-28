from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

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
    likes_count = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)

    def get_likes_count(self, obj):
        return models.MovieLike.objects.filter(movie=obj).count()

    def get_reviews_count(self, obj):
        return models.Review.objects.filter(movie=obj).count()


    class Meta:
        model = models.Movie
        fields = ('id', 'title', 'image', 'description', 'genre', 'movie_length', 'created_at', 'user', 'user_id', 'likes_count', 'reviews_count', 'reviews')


class MovieLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieLike
        fields = ('id', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user