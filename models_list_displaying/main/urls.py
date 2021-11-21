from django.contrib import admin
from django.urls import path, register_converter

from books.views import books_view, date_books_view
from books.converters import PubDateConverter


register_converter(PubDateConverter, 'pub_date')

urlpatterns = [
    path('books/', books_view, name='books'),
    path('books/<pub_date:value>/', date_books_view, name='date_books'),
    path('admin/', admin.site.urls),
]
