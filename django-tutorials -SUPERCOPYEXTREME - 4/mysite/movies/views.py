from django.shortcuts import render
from django.views import generic
from django.db import models
from movies.models import Film

#class movies(generic.ListView):
#    model = Film.title

# Create your views here.

def movies(request) :
    titles = Film.objects.all()
    context = {'titles': titles}
    return render(request,'movies/movies.html', context)
