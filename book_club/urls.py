from django.urls import path
from book_club.views import (
    BooksWithNotesView,
    MeetingListCreateView,
    NotesForBookView,
    NotesListCreateView
)


urlpatterns = [
    path('meetings/', MeetingListCreateView.as_view(), name='list-create-meeting'),
    path('notes/', NotesListCreateView.as_view(), name='list-create-notes'),
    path('notes/books/', BooksWithNotesView.as_view(), name='books-with-notes'),
    path('notes/book/<int:book_id>/', NotesForBookView.as_view(), name='notes-for-book'),
]