from django.views import View # importing View class
from django.shortcuts import render, get_object_or_404
from .models import Book #import book model from current dir

class BookList(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/book_list.html', {'books': books})
    
#BookList inherits from View. 
#Overrides the get() method which is executed when a GET verb request is made. 
# inside the get method, we run a querySet on the library of books. then render the html for a page of our books. 

class BookDetail(View):
    def get(self, request, pk): #include the pk for details
        # get_object_or_404 uses the pk to select the corresponding book.
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'books/book_detail.html', {'book': book})


# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books/book_list.html', {'books': books })

# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'books/book_detail.html', {'book':book })