from django.shortcuts import render
from django.http import HttpResponse
from .models import MainMenu

from .forms import BookForm, UserInfoForm
from django.http import HttpResponseRedirect

from .models import Book, User

from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from .filters import BookFilter
from .filters import MyBooksFilter

from django.db.models import Q


# Create your views here.


def index(request):
    # return HttpResponse("<h1 align='center'>Hello World</h1> <h2>This is a try </h2>")
    # return render(request, 'bookMng/displaybooks.html')
    return render(request,
                  'bookMng/home.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()

    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs

    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'myFilter': myFilter
                  }
                  )

# def search(request):
#     #         query=self.request.GET.get("query")
#     #         object_list=Book.objects.filter(
#     #             Q(name__icontains=query)
#     #         )
#     query=request.GET.get("query")
#     books = Book.objects.filter(
#         Q(name__icontains=query)
#     )
#
#
#     myFilter = BookFilter(request.GET, queryset=books)
#     books = myFilter.qs
#
#     for b in books:
#         b.pic_path = b.picture.url[14:]
#     return render(request,
#                   'bookMng/displaybooks.html',
#                   {
#                       'item_list': MainMenu.objects.all(),
#                       'books': books,
#                       'myFilter': myFilter
#                   }
#                   )


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)

    myFilter = MyBooksFilter(request.GET, queryset=books)
    books = myFilter.qs

    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'myFilter': myFilter
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def shoppingcart(request):
    books = Book.objects.filter(username=request.user)

    myFilter = MyBooksFilter(request.GET, queryset=books)
    books = myFilter.qs

    return render(request,
                  'bookMng/shoppingcart.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'myFilter': myFilter
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def shopping_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/shopping_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )




@login_required(login_url=reverse_lazy('login'))
def findbook(request):
    return render(request,
                  'bookMng/findbook.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/contact.html',
                  {
                      'form': form,
                      'submitted': submitted
                  }
                  )
  
  
def edit_info(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]

    if request.method == 'POST':
        try:
            book.username = request.user
            if request.FILES.get('picture') is not None:
                book.picture = request.FILES.get('picture')
            book.price = request.POST['price']
            book.name = request.POST['name']
            book.web = request.POST['web']
        except Exception:
            pass
        book.save()
        return HttpResponseRedirect('/mybooks')
    return render(request,
                  'bookMng/edit_info.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                  })


@login_required(login_url=reverse_lazy('login'))
def exchange(request, book_id):
    book = Book.objects.get(id=book_id)
    books = Book.objects.filter(username=request.user)
    book.pic_path = book.picture.url[14:]
    if request.method == 'POST':
        try:
            user_id = request.POST['exchange']
            user_book = Book.objects.get(id=user_id)
            temp = book.username
            book.username = user_book.username
            user_book.username = temp
        except Exception:
            pass
        book.save()
        user_book.save()
        return HttpResponseRedirect('/mybooks')

    return render(request,
                  'bookMng/exchange.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                      'books': books,
                  })


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def search(request):
    query = request.GET.get("query")
    book_list = Book.objects.filter(Q(name__icontains=query))

    return render(request,
                  'bookMng/searchresult.html',
                  {
                        'item_list': MainMenu.objects.all(),
                        'book_list': book_list
                  }
                  )



@login_required(login_url=reverse_lazy('login'))
def return_policy(request):
    return render(request,
                  'bookMng/return_policy.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def user_info(request):

    if request.method == 'POST':
        if User.objects.filter(username=request.user).exists():
            user = User.objects.get(username=request.user)
            form = UserInfoForm(request.POST, instance=user)
            if form.is_valid():
                userinfo = form.save(commit=False)
                try:
                    userinfo.username = request.user
                except Exception:
                    print('exception')
                    pass
                userinfo.save()
                return HttpResponseRedirect('/user_info')
        else:
            form = UserInfoForm(request.POST)
            if form.is_valid():
                userinfo = form.save(commit=False)
                try:
                    userinfo.username = request.user
                except Exception:
                    pass
                userinfo.save()
                return HttpResponseRedirect('/user_info')
    else:
        username = request.user

        if User.objects.filter(username=username).exists():

            user = User.objects.get(username=request.user )
            form = UserInfoForm(initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'street': user.street,
                'city': user.city,
                'state': user.state,
                'zipcode': user.zipcode,

            })
        else:
            print('ran2')
            form = UserInfoForm()

    return render(request,
                  'bookMng/user_info.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                  }
                  )
