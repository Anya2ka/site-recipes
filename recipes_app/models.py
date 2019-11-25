from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class Category(models.Model):

    name = models.CharField('Category name', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Dish(models.Model):

    image = models.ImageField(blank=True, null=True)
    name = models.CharField('Dish name', max_length=50)
    ingredients = ArrayField(JSONField())
    cooking_time = models.TimeField(blank=True, null=True)
    servings_number = models.PositiveSmallIntegerField(blank=True, default=1)
    cooking_method = models.TextField()
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(
        Category, related_name='dishes')
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='dishes')

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name
