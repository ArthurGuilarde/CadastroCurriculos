import requests
import random
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .filters import VagasFilter


# Create your views here.
def home(request):
  movies = ['M1', 'M2']

  # choice = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  # api_response = requests.get(f'http://www.omdbapi.com/?apikey=f7bb1681&i=tt128501{choice}')
  # movies.append(api_response.json()['Title'])

  # choice = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  # api_response = requests.get(f'http://www.omdbapi.com/?apikey=f7bb1681&i=tt12850{choice}8')
  # movies.append(api_response.json()['Title'])
  
  

  return render(request, 'home.html', context= { 
    'movies': movies, 
    'filter': VagasFilter(request.GET)})


def signup(request):
  template_name = 'signup.html'
  
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('core:signin')
  else:
    form = SignUpForm()

  context = {
    'form': form
  }
  return render(request, template_name, context)
