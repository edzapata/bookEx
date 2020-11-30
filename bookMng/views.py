from django.shortcuts import render
from django.http import HttpResponse
from .models import MainMenu

from .forms import BookForm
from django.http import HttpResponseRedirect

from .models import Book

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from .filters import BookFilter

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


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)

    myFilter = BookFilter(request.GET, queryset=books)
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


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
