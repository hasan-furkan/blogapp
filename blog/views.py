from django.shortcuts import render,  redirect
from django.http.response import HttpResponse
from blog.models import Blog, Category

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Full programming course Python",
            "image": "https://www.klasiksanatlar.com/img/sayfalar/b/1_1598452306_resim.png",
            "is_active": True,
            "is_home": False,
            "description": "Hello this course the best python programming"
        },
        {
            "id": 2,
            "title": "Full programming course JavaScript",
            "image": "https://www.klasiksanatlar.com/img/sayfalar/b/1_1598452306_resim.png",
            "is_active": True,
            "is_home": True,
            "description": "Hello this course the best python programming"
        },
        {
            "id": 3,
            "title": "Django And React",
            "image": "https://www.klasiksanatlar.com/img/sayfalar/b/1_1598452306_resim.png",
            "is_active": False,
            "is_home": True,
            "description": "Hello this course the best python programming"
        },
    ]
}

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, 'blog/index.html', context)


def blogs(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()

    }
    return render(request, 'blog/blogs.html', context) 


def blog_details(request, slug):
    if not request.user.is_authenticated:
        return redirect("login")
    blog = Blog.objects.get(slug=slug) 
    return render(request, 'blog/blog-details.html', {"blog": blog})

def blogs_by_category(request, slug):
    context = {
        # "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, 'blog/blogs.html', context) 