from rest_framework import serializers

from book.models import Book, Todo


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'book_title', 'book_author', 'publication_year']


class TodoSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    
    class Meta:
        model = Todo
        fields = ['id', 'book', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']