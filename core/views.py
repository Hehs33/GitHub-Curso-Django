from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request, 'index.html',{
        'title': 'Curso Django',
        'message': 'Curso Django 2024',
        'products': [
            {'title':'Camisa','price':50,'stock':True},
            {'title':'Pantalone','price': 100,'stock':False},
            {'title':'Gafas','price':35,'stock':True}
        ]
    })
