from django.contrib import admin
from .models import Author, Genre, Book, Review


class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    list_filter = ('last_name',)

class ReviewInline(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'amount', 'available', 'created', 'updated', 'cover')
    list_filter = ('author', 'available', 'created', 'updated')
    list_editable = ('price', 'amount', 'available', 'cover')
    inlines = [
        ReviewInline,
    ]
    
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
