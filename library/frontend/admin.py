from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
        fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Book, BookAdmin)