from django.contrib import admin
from libapp.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'no_of_copies', 'pages', 'price', 'published_date')
    list_display = ('title', 'pages', 'price')
    search_fields = ('title',)
    list_filter = ('price', 'pages')

admin.site.register(Book, BookAdmin)
