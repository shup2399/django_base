from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.
def create_book(request):
    BookInfo.objects.create(
        name='123',
        pub_date='2020-10-1',
        readcount=100,

    )
    return HttpResponse('created book!!!')