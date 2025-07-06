from django.contrib import admin

# Register your models here.
# blog/admin.py
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado', 'creado', 'autor')
    list_filter = ('publicado', 'creado')
    search_fields = ('titulo', 'contenido')

admin.site.register(Post, PostAdmin)

