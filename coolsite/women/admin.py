from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *                            # импорт для отображения в админке

class WomenAdmin(admin.ModelAdmin):               #дополнительные поля в админке
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    fields = ('get_html_photo2', 'slug', 'title', 'content', 'photo', 'is_published', 'time_create', 'time_update')   # fields at page of each object
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_photo2')
    list_display_links = ('id', )   # make links for editing
    search_fields = ('title', 'content')   # for searching in this columns
    list_editable = ('is_published', 'title')             # изменяемые в админке поля
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}  # автоматическое формирование slug в админке
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50")

    def get_html_photo2(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=500")

    get_html_photo.short_description = "Фото"

class CategoryAdmin(admin.ModelAdmin):              #дополнительные поля в админке
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',) # запятая обязательно тк кортеж!!!
    prepopulated_fields = {"slug": ("name",)}   # автоматическое формирование slug в админке

admin.site.register(Women, WomenAdmin)                       # импорт для отображения в админке
admin.site.register(Category, CategoryAdmin)
