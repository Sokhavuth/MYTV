import random
from django.shortcuts import render
from .settings import context
from .models import Movie


def index(request):
  movies = list( Movie.objects.all() )
  random.shuffle( movies )
  movie_list = movies[:6]
  
  id_list = [movie.video_id for movie in movie_list]

  context['id_list'] = id_list

  return render(request, 'index.html', context=context)
