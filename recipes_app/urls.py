from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.HomePageView.as_view(),
        name='home'
    ),
    path(
        'categories/<int:pk>/',
        views.CategoryDetailsPageView.as_view(),
        name='category-details'
    ),
    path(
        'dishes/<int:pk>/',
        views.DishDetailsPageView.as_view(),
        name='dish-details'
    ),
    path(
        'dishes/create',
        views.DishCreatePageView.as_view(),
        name='dish-create'
    ),
    path(
        'registration/',
        views.RegistrationPageView.as_view(),
        name='registration'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name="logout"),

    path(
        'login/',
        views.LoginView.as_view(),
        name="login"),

]
