from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission, User
from django.db.models import CharField, Model
from django.http import HttpResponse
from autoslug import AutoSlugField


class Books(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")  # 'verbose_name' for view in the admin panel
    slug = AutoSlugField(populate_from='name', unique_with='author')
    author = models.CharField(max_length=255, verbose_name="Автор(ы)")
    author_description = models.TextField(verbose_name='Описание автора / издательства')
    photo = models.ImageField(upload_to="books_photos", verbose_name="Фотография")
    publishing_house = models.ForeignKey('Publishing_house', on_delete=models.PROTECT, verbose_name="Издательство",
                                         null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил', blank=True, null=True)

    def __str__(self):  # function for showing field 'name' in SQL query (in CMD)
        return self.name  # SQL: Books.objects.all()

    def get_absolute_url(self):  # Use similar name ('get_absolute_url') for using in admin panel
        return reverse('book', kwargs={
            'book_slug': self.slug})  # функция reverse составляет url, ‘book’ - URL name from file ‘URL.PY’

    class Meta:
        verbose_name = 'Книги'  # название в админ панели
        verbose_name_plural = 'Книги'  # множ. число в админ панели
        ordering = ['name']  # сортировка, "-" - обр.порядок. Ordering for view at site


class Quotes(models.Model):
    quote = models.TextField(verbose_name="Цитата")
    book = models.ForeignKey(Books, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил', blank=True, null=True)

    def __str__(self):  # function for showing field 'quote' in SQL query
        return self.quote  # SQL: Quotes.objects.all()


class Read_books(models.Model):
    book = models.ForeignKey(Books, on_delete=models.PROTECT)
    status = models.TextField(verbose_name="Статус")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил', blank=True, null=True)
    booktype = models.ForeignKey('Booktype', on_delete=models.PROTECT, verbose_name="Вид книги", null=True)

    class Meta:
        verbose_name = 'Статус'  # название в админ панели
        verbose_name_plural = 'Статус'  # множ. число в админ панели

    def __str__(self):  # function for showing field 'quote' in SQL query
        return self.status  # SQL: Quotes.objects.all()


class Publishing_house(models.Model):
    publishing_house = models.TextField(verbose_name="Издательство")

    def __str__(self):  # function for showing field 'quote' in SQL query
        return self.publishing_house  # SQL: Quotes.objects.all()

    class Meta:
        verbose_name = 'Издательство'  # название в админ панели
        verbose_name_plural = 'Издательства'  # множ. число в админ панели


class Booktype(models.Model):
    booktype = models.TextField(verbose_name="Вид книги")

    def __str__(self):  # function for showing field 'quote' in SQL query
        return self.booktype  # SQL: Quotes.objects.all()

    class Meta:
        verbose_name = 'Вид'  # название в админ панели
        verbose_name_plural = 'Виды'  # множ. число в админ панели


class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")  # 'verbose_name' for view in the admin panel
    slug = AutoSlugField(populate_from='title', unique_with='user')
    photo = models.ImageField(upload_to="article_photos", verbose_name="Фотография", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил', blank=True, null=True)
    text = models.TextField(blank=True, verbose_name="Статья")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):  # function for showing field 'title' in SQL query
        return self.title  # SQL: Women.objects.all()

    def get_absolute_url(self):  # Use similar name ('get_absolute_url') for using in admin panel
        return reverse('text', kwargs={
            'text_slug': self.slug})  # функция reverse составляет url, ‘POST’ - URL name from file ‘URL.PY’

    class Meta:
        verbose_name = 'Статья'  # название в админ панели
        verbose_name_plural = 'Статьи'  # множ. число в админ панели
        ordering = ['-time_create', 'title']  # сортировка, "-" - обр.порядок. Ordering for view at site

class Measurements(models.Model):
    Date = models.DateField(auto_now_add=True, verbose_name="Дата замеров")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил')
    Shoulders = models.IntegerField(verbose_name="Плечи, см.")
    Chest = models.IntegerField(verbose_name="Грудь, см.")
    Waist = models.IntegerField(verbose_name="Талия, см.")
    Buttocks = models.IntegerField(verbose_name="Ягодицы, см.")
    Hips = models.IntegerField(verbose_name="Бёдра, см.")
    Weight = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Вес, кг.", blank=True, null=True)

    class Meta:
        verbose_name = 'Замеры тела' # название в админ панели
        verbose_name_plural = "Замеры тела"  # множ. число
        ordering = ['Date']

