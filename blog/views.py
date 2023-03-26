from django.shortcuts import render

posts = [
    {
        'author': 'Fadoua',
        'title': "Blog post 1",
        'content': 'First post content',
        'date_posted': 'March 26, 2023'
    },
    {
        'author': 'Fad',
        'title': "Blog post 2",
        'content': 'Second post content',
        'date_posted': 'April 27, 2023'
    },
]


def home(request):
    content={
        'posts' : posts
    }
    return render(request, 'blog/home.html', content)


def about(request):
    return render(request, 'blog/about.html', {'title':'About '})
