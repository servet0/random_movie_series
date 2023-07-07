from django.shortcuts import render
import random
from django.shortcuts import redirect
from .models import NumberMovie, NumberSeries

def random_movie(request):
    base_url = "https://www.imdb.com/title/"
    all_movies = NumberMovie.objects.values_list('numbermovie', flat=True)
    random_movie = random.choice(all_movies)
    movie_url = base_url + 'tt' + str(random_movie) + '/'
    return redirect(movie_url)

def random_series(request):
    base_url = "https://www.imdb.com/title/"
    all_series = NumberSeries.objects.values_list('numberseries', flat=True)
    random_series = random.choice(all_series)
    movie_url = base_url + 'tt' + str(random_series) + '/'
    return redirect(movie_url)


def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')


# Create your views here.

# Register your models here.
