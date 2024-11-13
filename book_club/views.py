from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from book_club.models import Meeting, Notes
from book_club.serializers import (
    BookWithNotesSerializer,
    MeetingSerializer,
    NotesSerializer
)
from book_club.utils import log_action
from book.models import Book


class MeetingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        book_id = request.data.get('book_id')
        description = request.data.get('description')
        start_time = request.data.get('start_time')
        duration = request.data.get('duration')

        book = Book.objects.filter(id=book_id).first()
        if not book:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        meeting = Meeting.objects.create(
            book=book,
            description=description,
            created_by=request.user,
            start_time=start_time,
            duration=duration
        )

        log_action(
            user=request.user,
            model_name='meeting',
            action='add',
            details=f"Added meeting for book {book.book_title} by {request.user.username}"
        )

        serializer = MeetingSerializer(meeting)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NotesListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        book_id = request.data.get('book_id')
        note = request.data.get('note')

        book = Book.objects.filter(id=book_id).first()
        if not book:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        notes_entry = Notes.objects.create(
            book=book,
            note=note,
            posted_by=request.user
        )

        log_action(
            user=request.user,
            model_name='notes',
            action='add',
            details=f"Added note for book {book.book_title} (id={book.id}) by {request.user.username}"
        )

        serializer = NotesSerializer(notes_entry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BooksWithNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.filter(notes__isnull=False).distinct()
        serializer = BookWithNotesSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotesForBookView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        notes = Notes.objects.filter(book=book)
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

