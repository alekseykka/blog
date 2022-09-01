from django.shortcuts import render
from blog.models import Post, Tag, Category, Review


# Create your views here.
def index(request):
    home = Post.objects.all()
    context = {
        'home': home,
        'title': 'Front page',
    }
    return render(request, "blog/index.html", context)
