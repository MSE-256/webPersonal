# blog/views.py
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    posts = Post.objects.filter(publicado=True)
    return render(request, 'blog/lista_posts.html', {'posts': posts})

# blog/views.py


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})
