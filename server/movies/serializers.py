from rest_framework_mongoengine import serializers

from movies.models import Movie


class MovieSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Movie
        fields = '__all__'