from django.db import models

optional = {
    "null": True,
    "blank": True
}

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    book_title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=255)

    def __str__(self):
        return self.book_title


class Todo(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='todos')
    notes = models.TextField(**optional)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Todo for {self.book.book_title}"
