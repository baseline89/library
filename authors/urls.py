from django.urls import path
from .views import AuthorList, AuthorDetail

app_name = 'authors'

urlpatterns = [
    path('', AuthorList.as_view(), name="authors-home"), 
    path('<int:pk>/', AuthorDetail.as_view(), name = "author-detail")
]