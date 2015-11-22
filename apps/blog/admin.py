# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Articulo, Categoria, Perfil


class ArtAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'fecha_pub')
	list_filter = ['fecha_pub']
	search_fields = ['titulo']

class PerAdmin(admin.ModelAdmin):
	fields = (('username', 'nombre', 'apellido', 'twitter', 'facebook', 'github', 'youtube', 'web', 'desc', 'desl', 'avatar'))
	list_display = ('username', 'nombre', 'apellido')

admin.site.register(Articulo, ArtAdmin)
admin.site.register(Categoria)
admin.site.register(Perfil, PerAdmin)