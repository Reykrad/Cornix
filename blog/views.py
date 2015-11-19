from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articulo

class IndexView(ListView):
	template_name = 'index.html'
	model = Articulo

class ArtDet(DetailView):
	template_name = 'art_detail.html'
	model = Articulo