from django.contrib import admin
from .models import Zone, Category, New
# Register your models here.

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    model = New
    list_display = ["title", "author", "created", "views", "shares"]
    search_fields = ['title', 'description']
    list_filter = ['author', 'created', 'zone', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'slug']
    search_fields = ["name"]


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    model = Zone
    list_display = ['name', 'slug']
    search_fields = ["name"]

