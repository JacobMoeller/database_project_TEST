from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from movies.models import Film
from movies.views import movies
from django.urls import re_path
from django.urls import path
from movies import views


#urlpatterns = [path('', ListView.as_view(queryset=Film.objects.all())
 #                                        (template_name="movies/movies.html")),
  #                   re_path('(?P<pk>(\d+))', DetailView.as_view(model=movie, template_name="movie/info.html"))]



#urlpatterns = [
 #   path('', views.movies, name='movies'),
  #  path('movies/', views.movies.as_view(), name='movies'),
#]

#urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.movies, name='movies'),
    
    #]

urlpatterns = [path('', ListView.as_view(queryset=Film.objects.all().order_by("title")[:25],
                                         template_name="movies/movies.html")),]

