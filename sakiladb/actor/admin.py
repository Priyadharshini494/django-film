from django.contrib import admin
from .models import *

# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Actor, ActorAdmin)
admin.site.register(Category, CategoryAdmin)