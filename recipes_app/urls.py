from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.HomePageView.as_view(),
        name='home'
    ),
    path(
        '<int:pk>/',
        views.CategoryDetailsPageView.as_view(),
        name='category-details'
    ),
    path(
        '<int:category_pk>/dishes/<int:dish_pk>/',
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
]
