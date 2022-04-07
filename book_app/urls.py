"""book_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views, api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('book-search/', views.book_search),
    path('book-add/', views.book_add),
    path('add-author/', views.author_add, name="author_add"),
    path('book/<int:pk>', views.book_view, name="book_view"),
    path('get-books/', views.get_books),
    path('api/books_api_view/', api_views.books_api_view, name="books_api_view"),
    path('api/books_search/', api_views.books_search, name='books_search'),
]
