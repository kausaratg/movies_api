from django.shortcuts import render
from rest_framework import viewsets
from movies.serializers import MovieSerializer
from movies.models import Movie
# Create your views here.
class movieview(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    
