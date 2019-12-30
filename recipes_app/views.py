from datetime import timedelta

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, reverse
from django.views import View
from django.views.generic import DetailView, FormView, ListView

from .forms import DishForm, IngredientsForm, SignUpForm
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


class DishDetailsPageView(DetailView, FormView):
    model = Dish
    template_name = "recipes_app/dish_details.html"
    form_class = DishForm

    def get_success_url(self):
        return reverse('dish-details', kwargs=self.kwargs)

    def get_initial(self):
        obj = self.get_object()

        hours = obj.cooking_time.seconds // 3600
        minutes = (obj.cooking_time.seconds // 60) % 60

        return {
            'cooking_time_hours': hours,
            'cooking_time_minutes': minutes,
            **model_to_dict(obj),
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ingredients = self.get_object().ingredients

        context['ingredients_forms'] = (
            formset_factory(
                IngredientsForm,
                extra=0 if ingredients else 1
            )(
                initial=ingredients
            )
        )

        return context

    def form_valid(self, form):
        ingredients_form = formset_factory(IngredientsForm)(self.request.POST)

        categories = form.cleaned_data.pop('categories')
        ct_hours = form.cleaned_data.pop('cooking_time_hours')
        ct_minutes = form.cleaned_data.pop('cooking_time_minutes')

        obj = self.get_object()

        for key, value in form.cleaned_data.items():
            setattr(obj, key, value)

        obj.categories.set(categories)
        obj.ingredients = ingredients_form.cleaned_data
        obj.cooking_time = timedelta(hours=ct_hours, minutes=ct_minutes)

        obj.save()

        return super().form_valid(form)

    def delete(self, *args, **kwargs):
        obj = self.get_object()
        obj.delete()

        return JsonResponse({
            'ok': True,
            'message': 'Dish with ID \'{id}\' successfully deleted'.format(
                id=kwargs['pk']
            )
        })


class RegistrationPageView(FormView):
    form_class = SignUpForm
    template_name = "recipes_app/registration.html"
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)


class DishCreatePageView(LoginRequiredMixin, FormView):
    template_name = "recipes_app/dish_create.html"
    form_class = DishForm

    def get_success_url(self):
        return reverse('dish-details', kwargs={
            'pk': self.dish.pk
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


class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'ok': True})
        else:
            return JsonResponse({'ok': False})
