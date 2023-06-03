from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.authors, name="authors-home"), 
    path('<int:pk>/', views.author_detail, name = "author-detail")
]