from rest_framework import serializers
from book_club.models import Meeting, Notes
from book.models import Book
from book.serializers import BookSerializer


class MeetingSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Meeting
        fields = ['id', 'book', 'description', 'created_by', 'start_time', 'duration']
        read_only_fields = ['created_by']


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'book', 'posted_by', 'note']
        read_only_fields = ['posted_by']


class BookWithNotesSerializer(serializers.ModelSerializer):
    notes = NotesSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['isbn', 'book_title', 'book_author', 'publication_year', 'publisher', 'notes']
