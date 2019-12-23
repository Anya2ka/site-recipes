from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from markdown import markdown


class Category(models.Model):

    name = models.CharField('Category name', max_length=50)
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Dish(models.Model):

    image = models.ImageField(blank=True, null=True)
    name = models.CharField('Dish name', max_length=50)
    ingredients = ArrayField(JSONField(), blank=True, default=list)
    cooking_time = models.DurationField(blank=True, null=True)
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

    def save(self, *args, **kwargs):
        if self.cooking_method:
            self.cooking_method = markdown(self.cooking_method)

        if self.description:
            self.description = markdown(self.description)

        return super(Dish, self).save(*args, **kwargs)
