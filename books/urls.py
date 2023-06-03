from django.urls import path
from .views import BookList, BookDetail 

app_name = 'books'

urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail')
]
