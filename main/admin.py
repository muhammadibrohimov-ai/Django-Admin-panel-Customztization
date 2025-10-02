from django.contrib import admin
from .models import Author, Book
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ['name', 'year', 'email', 'address', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['year', 'created_at']
    list_display_links = ['name', 'year']
    list_editable = ['email', 'address']
    
@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ['title', 'genre', 'author', 'year', 'price']
    search_fields = ['author__name', 'title', 'genre']
    list_filter = ['year', 'author', 'created_at', 'genre']
    list_display_links = ['title', 'year', 'genre', 'author']
    list_editable = ['price']
    autocomplete_fields = ['author']
