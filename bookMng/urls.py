from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('shopping_delete/<int:book_id>', views.shopping_delete, name='shopping_delete'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('findbook', views.findbook, name='findbook'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('return_policy', views.return_policy, name='return_policy'),

]

