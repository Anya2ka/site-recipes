from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "recipes_app/home.html"


class CategoryDetailsPageView(TemplateView):
    template_name = "recipes_app/category.html"


class DishDetailsPageView(TemplateView):
    template_name = "recipes_app/dish_details.html"


class RegistrationPageView(TemplateView):
    template_name = "recipes_app/registration.html"


class DishCreatePageView(TemplateView):
    template_name = "recipes_app/dish_create.html"
