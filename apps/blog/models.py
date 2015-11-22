from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Categoria(models.Model):
	ncat = models.CharField(max_length=15)

	def __unicode__(self):
		return self.ncat

	def __str__(self):
		return self.ncat

class Perfil(models.Model):
	username = models.CharField('Nombre de usuario', max_length=10)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	twitter = models.URLField(max_length=40, blank=True)
	facebook = models.URLField(max_length=100, blank=True)
	github = models.URLField(max_length=50, blank=True)
	youtube = models.URLField(max_length=100, blank=True)
	web = models.URLField(max_length=100, blank=True)
	desc = models.TextField('Descripcion Corta', max_length=500, blank=True)
	desl = models.TextField('Descripcion Larga', max_length=1500, blank=True)
	avatar = models.URLField(blank=True)

	def __unicode__(self):
		return self.username

	def __str__(self):
		return self.username

class Articulo(models.Model):
	autor = models.ForeignKey(Perfil)
	titulo = models.CharField(max_length=200)
	contenido = RichTextField(config_name='ckeditor')
	fecha_pub = models.DateTimeField(editable=False, auto_now=True)	
	slug = models.SlugField(editable=False)
	cat = models.ManyToManyField(Categoria)

	def __unicode__(self):
		return self.titulo

	def save(self, *arg, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Articulo, self).save(*arg, **kwargs)