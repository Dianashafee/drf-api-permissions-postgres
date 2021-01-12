
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializer import MoviesSerializer
from .models import Movies
from .permissions import PermissionsClass

# Create your views here.
class MoviesListView(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (PermissionsClass,IsAuthenticated)

class MoviesDetailsView(RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (PermissionsClass,IsAuthenticated)