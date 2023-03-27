import os
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

# setx OMDB_API_KEY "your_api_key"
OMDB_API_KEY = os.environ['OMDB_API_KEY']

def index(request):
    """
    Renders the index.html template.
    """
    return render(request, 'index.html')

def home(request):
    """
    Renders the home.html template.
    """
    return render(request, 'home.html')

def movie_detail(request):
    """
    Renders the movie_detail.html template which displays movie information.
    Uses the OMDb API to get movie information based on the user's input.
    """
    # setx OMDB_API_KEY "your_api_key"
    movie_data_keys = []
    url = 'http://www.omdbapi.com/?apikey={}&t={}'.format(OMDB_API_KEY, 'Titanic')
    movie_data = get__omdb_movie_data(url)
    if movie_data:
        movie_data_keys = movie_data.keys()
    if request.method == 'POST':
        url = 'http://www.omdbapi.com/?apikey={}'.format(OMDB_API_KEY)
        if 'movie_name' in request.POST:
            movie_name = request.POST.get('movie_name')
            if movie_name:
                url += '&t={}'.format(movie_name)
        if 'movie_year' in request.POST:
            movie_year = request.POST.get('movie_year')
            if movie_year:
                url += '&y={}'.format(movie_year)
        movie = get__omdb_movie_data(url)
        return render(request, 'movie_detail.html', {'movie': movie, 'movie_data_keys': movie_data_keys})
    return render(request, 'movie_detail.html', {'movie_data_keys': movie_data_keys})


def movie_search(request):
    """
    Renders the movie_search.html template which displays movie lookup information.
    Uses the OMDb API to get movie lookup information based on the user's input.
    """
    if request.method == 'POST':
        movie = None
        if 'movie_name' in request.POST:
            movie_name = request.POST.get('movie_name')
            if movie_name:
                url = 'http://www.omdbapi.com/?apikey={}&t={}'.format(OMDB_API_KEY, movie_name)
                movie = get__omdb_movie_data(movie_name)
        return render(request, 'movie_search.html', {'movie': movie})
    return render(request, 'movie_search.html')

@require_GET
def autocomplete_movie_search(request):
    results = []
    if request.method == 'GET':
        if 'q' in request.GET:
            query = request.GET.get('q', '')
            if query:
                url = 'http://www.omdbapi.com/?apikey={}&s={}'.format(OMDB_API_KEY, query)
                result = get__omdb_movie_data(url)
                if 'Search' in result:
                    search_results = result['Search']
                    # Only keep the first 5 search results
                    for r in search_results[:5]:
                        # Check if the result contains the necessary fields
                        if 'Title' in r and 'Year' in r and 'Poster' in r:
                            results.append({
                                'label': '{} ({})'.format(r['Title'], r['Year']),
                                'image_url': r['Poster'],
                            })
    # Filter the results that do not match the query
    results = [r for r in results if isinstance(r, dict) and query.lower() in r.get('label', '').lower()]
    # Return the first 5 results
    return JsonResponse(results[:5], safe=False)


def get__omdb_movie_data(url):
    """
    Uses the OMDb API to get movie information based on the user's input.
    """
    response = requests.get(url)
    movie = response.json()
    return movie