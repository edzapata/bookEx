import django_filters
from django_filters import CharFilter
import widget_tweaks
from .models import *


class BookFilter(django_filters.FilterSet):
    book_name = CharFilter(field_name="name", lookup_expr='icontains', label='Book Title')
    user = CharFilter(field_name="username__username", lookup_expr='icontains', label='Posted By')
    
class MyBooksFilter(django_filters.FilterSet):
    book_name = CharFilter(field_name="name", lookup_expr='icontains', label='Book Title')


class Meta:
    model = Book
    fields = []
    exclude = ['picture', 'pic_path', 'publishdate']
