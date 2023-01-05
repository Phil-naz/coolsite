from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.forms import Textarea, ModelForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): # it is for "ВЫБРАТЬ" instead of "---"
        super().__init__(*args, **kwargs)
        self.fields['publishing_house'].empty_label = "ВЫБРАТЬ"

    class Meta:  # this class for formatting view of fields
        model = Books
        fields = ['name_ru', 'name_en', 'author_ru', 'author_en', 'photo', 'author_description_ru', 'author_description_en', 'publishing_house']
        widgets = {  # this is for individual design fields
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'author': forms.TextInput(attrs={'class': 'form-input'}),
            'author_description': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }

    def clean_name(self):  # for validation field. In name after _ field name
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return name


class AddTextForm(forms.ModelForm): # it is for "Категория не выбрана" шnstead of "---"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_ru'].empty_label = "Категория не выбрана"

    class Meta:
        model = Articles
        fields = ['title_ru', 'title_en', 'text_ru', 'text_en', 'photo', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return


class AddMeasurements(forms.ModelForm):
    class Meta:  # this class for formatting view of fields
        model = Measurements
        fields = ['Shoulders', 'Chest', 'Waist', 'Buttocks', 'Hips', 'Weight']
        widgets = {  # this is for individual design fields
            'Shoulders': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Chest': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Waist': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Buttocks': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Hips': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Weight': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': None, 'type': 'number',}),
        }
