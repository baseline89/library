from django.shortcuts import render, get_object_or_404
from .models import Author

def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_profiles.html', context = {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'authors/author_detail.html', context = {'author': author})