from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'get_html_photo')
    fields = ('name', 'author', 'photo')   # fields at page of each object
    list_display_links = ('author',)  # make links for editing
    search_fields = ('name', 'author')  # for searching in this columns
    list_editable = ('name',)   # function for edit data in admin panel
    list_filter = ('publishing_house',)


    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50")

    get_html_photo.short_description = "Миниатюра"

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_display_links = ('id', 'status')  # make links for editing

class BooktypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'booktype')
    list_display_links = ('id', 'booktype')  # make links for editing

class Publishing_houseAdmin(admin.ModelAdmin):
    list_display = ('id', 'publishing_house')
    list_display_links = ('id', 'publishing_house')  # make links for editing




admin.site.register(Books, BooksAdmin)
admin.site.register(Booktype, BooktypeAdmin)
admin.site.register(Publishing_house, Publishing_houseAdmin)

