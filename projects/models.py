from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class CategoryProj(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='gallery_images')  # Cambio de 'gallery_images'
    image = models.ImageField(verbose_name='Imagen', upload_to='gallery/')
      
    def __str__(self):
        return self.project.title  # Cambiar al campo que contiene el nombre del proyecto

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = RichTextField(verbose_name='Contenido completo')
    published = models.DateTimeField(verbose_name='Fecha de Publicación', default=now)
    categories = models.ManyToManyField(CategoryProj, verbose_name='Categorías', related_name='projects')  # Cambio de 'projects'
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
