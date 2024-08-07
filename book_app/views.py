from django.shortcuts import render, redirect

from .forms import AuthorForm,BookForm


# Create your views here.
from .models import Book

# def createbook(request):
#     if request.method=='POST':
#         title=request.POST.get('title')
#         price= request.POST.get('price')
#         book= Book(title=title,price=price)
#         book.save()
#         return render(request,'book.html')
def listbook(request):

    books=Book.objects.all()

    return render(request,'listbook.html',{'books':books})

def specificbook(request,books_id):
    books=Book.objects.get(id=books_id)

    return render(request,'specificbook.html',{'books':books})


# def updatebook(request,book_id):
#     book=Book.objects.get(id=book_id)
#
#     if request.method=='POST':
#
#         title = request.POST.get('title')
#         price = request.POST.get('price')
#
#         book.title=title
#         book.price=price
#
#         book.save()
#         return redirect('/')
#
#     return render(request,'updatebook.html',{'book':book})

def updatebook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        form= BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BookForm()
        return render(request,'book.html',{'form':form})


def deletebook(request,book_id):
    book=Book.objects.get(id=book_id)

    if request.method=='POST':
      book.delete()
      return redirect('/')

    return render(request,'deletebook.html',{'book':book})

def createbook(request):
    books=Book.objects.all()

    if request.method=='POST':
        form= BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= BookForm()
    return render(request,'book.html',{'form':form,'books':books})

def createauthor(request):
    if request.method=='POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form= AuthorForm()
    return render(request,'author.html',{'form':form})
