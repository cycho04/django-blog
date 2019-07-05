from django.shortcuts import render

posts = [
    {
        'author': 'CC',
        'title': 'Blog Post 1',
        'content': 'Content here',
        'date_posted': '7/4/2019'
    },
    {
        'author': 'CC',
        'title': 'Blog Post 2',
        'content': 'Content here for blog 2',
        'date_posted': '7/5/2019'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Testing'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
