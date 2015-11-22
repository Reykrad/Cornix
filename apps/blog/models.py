from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Categoria(models.Model):
	ncat = models.CharField(max_length=15)

	def __unicode__(self):
		return self.ncat

	def __str__(self):
		return self.ncat

class Articulo(models.Model):
	cat = models.ForeignKey(Categoria)
	titulo = models.CharField(max_length=200)
	contenido = RichTextField(config_name='ckeditor')
	fecha_pub = models.DateTimeField(editable=False, auto_now=True)	
	slug = models.SlugField(editable=False)

	def __unicode__(self):
		return self.titulo

	def save(self, *arg, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Articulo, self).save(*arg, **kwargs)