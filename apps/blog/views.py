# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apps.blog.models import Articulo, Categoria

class IndexView(ListView):
	queryset = Articulo.objects.order_by('-fecha_pub')
	context_object_name = 'queryset'
	template_name = 'index.html'
	model = Articulo
	paginate_by = 2

class ArtDet(DetailView):
	template_name = 'art_detail.html'
	model = Articulo