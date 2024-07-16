from django.contrib import admin
from .models import *
from film.models import Film

class Filmadmin(admin.ModelAdmin):
    list_display = ["title","description","release_year","rental_duration","rental_rate","length","replacement_cost","rating","special_features","is_featured"]

admin.site.register(Film, Filmadmin)
admin.site.register(FilmActor)
admin.site.register(FilmCategory)
admin.site.register(FilmText)
admin.site.register(Language)
