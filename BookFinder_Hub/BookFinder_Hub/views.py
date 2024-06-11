from django.http import HttpResponse
from django.shortcuts import render
from BookFinder_Hub.functions import flipkart_scrap
import json

def home(request):
    book = ""
    author = ""
    publisher = ""
    try:
        if request.method == 'POST':
            book = request.POST.get('book')
            author = request.POST.get('author')
            publisher = request.POST.get('publisher')
            rec = True
    except:
        print("Not assigned")

 #   amazon = amazon_scrap(book = book, author = author, publisher = publisher)
    flipkart = flipkart_scrap(book = book, author = author, publisher = publisher)

    data = {'available': False, 'sites': [flipkart, None, flipkart, None, None, flipkart]}
#    data_json = json.dumps(data)
    return render(request, 'index.html', data)


