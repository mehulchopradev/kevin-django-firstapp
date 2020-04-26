from django.contrib import admin
from libapp.models import Book, PublicationHouse, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'no_of_copies', 'pages', 'price', 'published_date', 'publication_house')
    list_display = ('title', 'pages', 'price')
    search_fields = ('title',)
    list_filter = ('price', 'pages')

    inlines = [ReviewInline]

admin.site.register(Book, BookAdmin)
admin.site.register(PublicationHouse)