from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'student_class', 'subject', 'upload_date')
    list_filter = ('student_class', 'subject')
    search_fields = ('title', 'subject')