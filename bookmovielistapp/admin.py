from django.contrib import admin
from .models import BookMovieList, ListItem, Chapter
# Register your models here.
admin.site.register(Chapter)
admin.site.register(BookMovieList)
admin.site.register(ListItem)