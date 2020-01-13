from django.contrib import admin
from .models import Author,Projects

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags')

admin.site.register(Author)
admin.site.register(Projects)
