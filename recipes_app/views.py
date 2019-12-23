from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import IngredientsForm, NewDishForm
from .models import Category, Dish


class HomePageView(ListView):
    template_name = "recipes_app/home.html"
    model = Category


class CategoryDetailsPageView(ListView):
    template_name = "recipes_app/category.html"

    def dispatch(self, request, *args, **kwargs):
        get_object_or_404(Category, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Dish.objects.filter(categories=self.kwargs['pk'])


class DishDetailsPageView(DetailView):
    model = Dish
    template_name = "recipes_app/dish_details.html"
    pk_url_kwarg = 'dish_pk'


class RegistrationPageView(TemplateView):
    template_name = "recipes_app/registration.html"


class DishCreatePageView(LoginRequiredMixin, FormView):
    template_name = "recipes_app/dish_create.html"
    form_class = NewDishForm

    def get_success_url(self):
        return reverse('dish-details', kwargs={
            'dish_pk': self.dish.pk
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ingredients_forms'] = formset_factory(IngredientsForm)

        return context

    def form_valid(self, form):
        ingredients_form = formset_factory(IngredientsForm)(self.request.POST)

        categories = form.cleaned_data.pop('categories')
        ct_hours = form.cleaned_data.pop('cooking_time_hours')
        ct_minutes = form.cleaned_data.pop('cooking_time_minutes')

        self.dish = Dish.objects.create(
            author=self.request.user,
            cooking_time=timedelta(hours=ct_hours, minutes=ct_minutes),
            ingredients=ingredients_form.cleaned_data,
            **form.cleaned_data
        )

        self.dish.categories.set(categories)
        self.dish.save()

        return super().form_valid(form)
