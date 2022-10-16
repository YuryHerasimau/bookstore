from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    # Rename <object_list> to a friendlier name
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    # Rename <object> to a friendlier name
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
