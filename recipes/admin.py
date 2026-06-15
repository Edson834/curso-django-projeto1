from django.contrib import admin
from .models import Category, Recipe

@admin.register(Recipe)

class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)


