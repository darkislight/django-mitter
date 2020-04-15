from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Maaz',
        'title': 'post 1',
        'content': 'first post content',
        'date_posted': 'april 15,2020'
    },

    {
        'author':'Jack',
        'title':'post 2',
        'content':'second post content',
        'date_posted':'april 17,2020'
    }
]




def home(request):
    context = {
    'posts':posts
    }

    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
