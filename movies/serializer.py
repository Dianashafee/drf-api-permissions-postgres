
from rest_framework import serializers

from .models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description', 'movie_type')
        model = Movies