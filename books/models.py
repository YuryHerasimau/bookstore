import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Genre(models.Model):
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True)
    title = models.CharField(max_length=200, db_index=True, help_text="Enter genre's name")

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_genre_url(self):
        return reverse('index_by_genre', args=[str(self.slug)])


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=False)
    date_of_death = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Enter short book description", blank=True)
    genre = models.ManyToManyField(Genre, help_text="Select genres", related_name="books")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    # Insteaf of {% url 'book_detail' book.pk %}
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.review
