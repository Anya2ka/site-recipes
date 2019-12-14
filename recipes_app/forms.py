from django import forms

from .models import Category


class NewDishForm(forms.Form):
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
