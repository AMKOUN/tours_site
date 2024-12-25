from django.shortcuts import render
from .models import Post


def index(request):
    elements = Post.objects.all()
    context = {
        'elements': elements
    }
    return render(request, 'DIYtour/index.html', context)
