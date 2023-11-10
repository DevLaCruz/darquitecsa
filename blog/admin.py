from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CateforyAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('name', 'created')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('title', 'author', 'published')
    ordering=('author','published')
    search_fields=('title', 'content')

admin.site.register(Category, CateforyAdmin)
admin.site.register(Post, PostAdmin)