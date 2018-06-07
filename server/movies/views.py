from django.shortcuts import render

# Create your views here.
from rest_framework_mongoengine import viewsets

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()