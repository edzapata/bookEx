from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('findbook', views.findbook, name='findbook'),
    path('edit_info/<int:book_id>', views.edit_info, name='edit_info'),
    path('exchange/<int:book_id>', views.exchange, name='exchange'),
    path('exchange', views.exchange, name='exchange'),
]

