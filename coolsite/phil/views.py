from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


from .utils import *
from .models import *
from .forms import *

# backup copy 2023 January 19. Commit 03/2023: adding & comparison of measurements

#  main menu  is in 'base.html'
def test(request):
    context = {
        'title': 'Bootstrap',
    }
    return render(request, 'phil/test.html', context=context)

def measurements(request):
    last = Measurements.objects.order_by('-Date')[0]  # for last user's value
    if request.method == 'POST':
        form = AddMeasurements(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('measurements')
    else:
        form = AddMeasurements()
    context = {
        'title': 'Add measurements',
        'measurements': Measurements.objects.filter(user=request.user),
        'form': form,
        'last':  last, # for last user's value
    }
    return render(request, 'phil/measurements.html', context=context)

def comparison(request, comp_pk):
    last = Measurements.objects.filter(user=request.user).order_by('-Date')[0]   # for last user's value
    meas = get_object_or_404(Measurements, pk=comp_pk)
    dif_Shoulders = int(last.Shoulders) - int(meas.Shoulders)
    dif_Chest = int(last.Chest) - int(meas.Chest)
    dif_Waist = int(last.Waist) - int(meas.Waist)
    dif_Buttocks = int(last.Buttocks) - int(meas.Buttocks)
    dif_Hips = int(last.Hips) - int(meas.Hips)
    dif_Weight = round(float(last.Weight) - float(meas.Weight), 2)
    context = {
        'title': 'Comparison measurements',
        'comp': comp_pk.title(),
        'last': last,  # for last user's value
        'meas': meas,
        'dif_Shoulders': dif_Shoulders,
        'dif_Chest': dif_Chest,
        'dif_Waist': dif_Waist,
        'dif_Buttocks': dif_Buttocks,
        'dif_Hips': dif_Hips,
        'dif_Weight': dif_Weight,
    }
    return render(request, 'phil/comparison.html', context=context)


class BooksList(DataMixin, ListView):
    paginate_by = 5   # count of elements on the page
    model = Books
    template_name = 'phil/books.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Книги')
        return dict(list(context.items()) + list(c_def.items()))   # combine (объединяем) classes ‘context’ & c_def (local data for transferring)


class ShowBook(DataMixin, DetailView):
    model = Books
    template_name = 'phil/book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):  # for transfer dynamic data
        context = super().get_context_data(**kwargs)  # mandatory (обязательное) condition
        c_def = self.get_user_context(title= context['book'])
        return dict(list(context.items()) + list(c_def.items()))   # combine (объединяем) classes ‘context’ & c_def (local data for transferring)

class AddBook(LoginRequiredMixin, DataMixin, CreateView):  # 'LoginRequiredMixin' on first place!!!
   # 'LoginRequiredMixin' make this class only for authorized users
   form_class = AddBookForm
   template_name = 'phil/addbook.html'
   login_url = reverse_lazy('admin:index')  # redirecting for unauthorized users to authorization page
   # show mistake 403 for unauthorized users: 'raise_exception = True
   def get_context_data(self, *, object_list=None, **kwargs):
       context = super().get_context_data(**kwargs)
       c_def = self.get_user_context(title= 'Add a book')
       return dict(list(context.items()) + list(c_def.items()))   # combine (объединяем) classes ‘context’ & c_def (local data for transferring)


def about(request):
    context = {
        'title': 'Philip Nazarenko: about me',
    }
    return render(request, 'phil/about.html', context=context)

def about_analytics(request):
    context = {
        'title': 'Аналитика (с использованием Excel, SQL, Python)',
    }
    return render(request, 'phil/about_analytics.html', context=context)

def about_django(request):
    context = {
        'title': 'Разработка веб-проектов с использованием фреймворка Django (Python)',
    }
    return render(request, 'phil/about_django.html', context=context)

def login(request):
    return HttpResponse('<h1>Phil app’s login page</h1>')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm   # standard form in Django 'AuthenticationForm'
    template_name = 'phil/login.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Авторизация')   # class 'DataMixin'
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):   # URL for redirecting authorized user
        return reverse_lazy('phil_home')

def phil_logout(request):
    logout(request)
    return redirect('phil_login')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm   # standard form in Django 'UserCreationForm'
    template_name = 'phil/register.html'
    success_url = reverse_lazy('phil_login')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Регистрация')   # class 'DataMixin'
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):   # function if registration successfully
        user = form.save()
        login(user)   # maybe 2 arguments, (self.request, user)
        return redirect('phil_home')


def showtexts(request):
    context = {
        'title': 'Заметки',
        'menu': menu,
        'texts': Articles.objects.all(),
    }
    return render(request, 'phil/texts.html', context=context)


def addtext(request):
    if request.method == 'POST':
        form = AddTextForm(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('texts')
    else:
        form = AddTextForm()
    return render(request, 'phil/addtext.html', {'form': form, 'menu': menu, 'title': 'Добавление заметки'})


def login(request):
    return HttpResponse('<h1>Phil app’s login page</h1>')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm   # standard form in Django 'AuthenticationForm'
    template_name = 'phil/login.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Авторизация')   # class 'DataMixin'
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):   # URL for redirecting authorized user
        return reverse_lazy('phil_home')

def phil_logout(request):
    logout(request)
    return redirect('phil_login')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm   # standard form in Django 'UserCreationForm'
    template_name = 'phil/register.html'
    success_url = reverse_lazy('phil_login')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Регистрация')   # class 'DataMixin'
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):   # function if registration successfully
        user = form.save()
        login(user)   # maybe 2 arguments, (self.request, user)
        return redirect('phil_home')


def showtexts(request):
    context = {
        'title': 'Заметки',
        'texts': Articles.objects.all(),
    }
    return render(request, 'phil/texts.html', context=context)


    return HttpResponse("Show all texts")

def text(request, text_slug):
    art = get_object_or_404(Articles, slug=text_slug)
    context = {
        'text': art,
        'title': art.title,
    }
    return render(request, 'phil/text.html', context=context)

def addtext(request):
    if request.method == 'POST':
        form = AddTextForm(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('texts')
    else:
        form = AddTextForm()
    return render(request, 'phil/addtext.html', {'form': form, 'title': 'Добавление заметки'})

