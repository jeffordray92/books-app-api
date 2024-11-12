from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound

from book.models import Book, Todo
from book.serializers import BookSerializer, TodoSerializer


class BookSearchView(APIView):

    def get(self, request):
        search_query = request.query_params.get('q', '')
        books = Book.objects.filter(
            Q(book_title__icontains=search_query) |
            Q(book_author__icontains=search_query)
        )
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_books = paginator.paginate_queryset(books, request)
        
        serializer = BookSerializer(paginated_books, many=True)
        return paginator.get_paginated_response(serializer.data)


class TodoListCreateView(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        book_id = request.data.get('book_id')
        isbn = request.data.get('isbn')
        notes = request.data.get('notes', '')

        book = None
        if book_id:
            book = Book.objects.filter(id=book_id).first()
        elif isbn:
            book = Book.objects.filter(isbn=isbn).first()

        if not book:
            raise NotFound("Book not found.")

        todo = Todo.objects.create(book=book, notes=notes)
        serializer = TodoSerializer(todo)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

