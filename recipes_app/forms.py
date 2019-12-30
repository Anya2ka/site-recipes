from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Category


class DishForm(forms.Form):
    name = forms.CharField(
        label='Название блюда', max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'placeholder': 'Добавьте описание блюда',
                'class': 'form-control'
            }
        ),
        required=False
    )
    cooking_method = forms.CharField(
        label='Способ приготовления',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте способ приготовления'
            }
        )
    )
    categories = forms.ModelMultipleChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control'},
        )
    )

    servings_number = forms.IntegerField(
        max_value=50,
        min_value=1,
        initial=1,
        label='Количество порций',
        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'custom-file-input'}),
        label='.png, .jpeg, gif...',
        required=False)

    cooking_time_hours = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        ),
        min_value=0,
        initial=0,
        label='Часы',
        required=False
    )

    cooking_time_minutes = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        ),
        min_value=0,
        max_value=59,
        initial=0,
        label='Минуты',
        required=False
    )


class IngredientsForm(forms.Form):
    name = forms.CharField(
        label='Ингридиенты',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    qty = forms.CharField(
        label='Количество',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='E-mail',
        max_length=254,
        help_text='Required. Inform a valid email address.',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        help_text=(
            'Подтверждение пароля. Пароль должен быть таким же как и выше'
        ),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', )
