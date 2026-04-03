from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        to='recipes.Category', on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        to='recipes.Author', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
