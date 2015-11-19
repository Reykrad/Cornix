from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Categorias(models.Model):
	ncate = models.CharField(max_length=15)

	def __str__(self):
		return self.ncate

class Articulo(models.Model):
	cat = models.ForeignKey(Categorias)
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	fecha_pub = models.DateField(editable=False, auto_now=True)
	slug = models.SlugField(editable=False)

	def __unicode__(self):
		return self.titulo

	def save(self, *arg, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Articulo, self).save(*arg, **kwargs)


#Perfil de usuario
# class Perfil(models.Model):
# 	user = models.ForeignKey(User, unique=True)
# 	twitter = models.CharField(max_length=120)