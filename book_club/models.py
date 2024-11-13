from django.db import models
from django.conf import settings

from book.models import Book


class Meeting(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='meetings')
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meetings')
    start_time = models.DateTimeField()
    duration = models.CharField(max_length=20)

    def __str__(self):
        return f"Meeting for {self.book.book_title} by {self.created_by.username}"


class Notes(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes')
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()

    class Meta:
        verbose_name_plural = "Notes"

    def __str__(self):
        return f"Note on {self.book.book_title} by {self.posted_by.username} "


class Logs(models.Model):
    """
    Note: We can add other actions here, but since we only have adding of notes and meetings
    for now, I've only added 'add' action choice
    """
    ACTION_CHOICES = [
        ('add', 'Add'),
    ]
    MODEL_CHOICES = [
        ('meeting', 'Meeting'),
        ('notes', 'Notes')
    ]
    model_name = models.CharField(max_length=7, choices=MODEL_CHOICES)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    class Meta:
        verbose_name_plural = "Logs"

    def __str__(self):
        return f"{self.action} action on {self.model_name} by {self.user}"