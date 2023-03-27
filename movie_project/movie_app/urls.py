from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.movie_detail, name='movie_detail'),
    path('search/', views.movie_search, name='movie_search'),
    path('autocomplete-movie-search/', views.autocomplete_movie_search, name='autocomplete_movie_search'),
]