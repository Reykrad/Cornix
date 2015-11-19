from django.contrib import admin
from .models import Articulo, Categorias

class ArtAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'cat', 'fecha_pub')
	list_filter = ['fecha_pub']
	search_fields = ['titulo']
admin.site.register(Articulo, ArtAdmin)
admin.site.register(Categorias)