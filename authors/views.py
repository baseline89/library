from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Author

class AuthorList(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'authors/author_profiles.html', {'authors': authors})

class AuthorDetail(View):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return render(request, 'authors/author_detail.html', {'author': author})





# from django.shortcuts import render, get_object_or_404
# from .models import Author

# def authors(request):
#     authors = Author.objects.all()
#     return render(request, 'authors/author_profiles.html', context = {'authors': authors})

# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     return render(request, 'authors/author_detail.html', context = {'author': author})