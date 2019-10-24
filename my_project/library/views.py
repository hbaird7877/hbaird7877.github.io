from django.shortcuts import render
from .models import Book

# Create your views here.
def list_books(request):
  book = Book.objects.all()
  return render(request, 'books/book_list.html', {'book':book})