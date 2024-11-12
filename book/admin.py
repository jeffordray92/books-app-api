from django.contrib import admin
from book.models import Book, Todo


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'book_title', 'book_author', 'publication_year', 'publisher')
    search_fields = ('book_title', 'book_author', 'isbn')
    list_filter = ('publication_year', 'publisher')


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'notes', 'created_at', 'updated_at')
    search_fields = ('book__book_title', 'book__isbn')
    list_filter = ('created_at',)
