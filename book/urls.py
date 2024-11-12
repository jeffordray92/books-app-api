from django.urls import path

from book.views import (
    BookSearchView,
    TodoListCreateView
)


urlpatterns = [
    path('search/', BookSearchView.as_view(), name='book-search'),
    path('todo/', TodoListCreateView.as_view(), name='list-create-todo'),
]
