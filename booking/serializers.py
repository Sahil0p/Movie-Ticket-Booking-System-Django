from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Show, Booking

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "duration_minutes","poster"]

class ShowSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Show
        fields = ["id", "movie", "screen_name", "date_time", "total_seats"]

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    show = ShowSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "user", "show", "seat_number", "status", "created_at"]
