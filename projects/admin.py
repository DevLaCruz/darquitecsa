from django.contrib import admin
from .models import CategoryProj, GalleryImage, Project

# Definición de las clases de administración
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage

class ProjectAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ('title', 'published', 'created', 'updated')
    list_filter = ('categories',)
    search_fields = ('title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')


# Registrar los modelos y clases de administración
admin.site.register(CategoryProj, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(GalleryImage)
