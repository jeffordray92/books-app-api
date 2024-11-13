from django.contrib import admin
from book_club.models import Notes, Meeting, Logs


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'posted_by', 'note')
    search_fields = ('book__book_title', 'posted_by__username', 'note')
    list_filter = ('posted_by', 'book')


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'created_by', 'start_time', 'duration')
    search_fields = ('book__book_title', 'created_by__username', 'description')
    list_filter = ('created_by', 'start_time', 'duration')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('action', 'model_name', 'user', 'timestamp', 'details')
    list_filter = ('action', 'model_name', 'user')
    search_fields = ('details', 'user__username')
