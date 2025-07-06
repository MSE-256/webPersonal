# from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu
#change
from django.shortcuts import render
from .models import Post
from django.shortcuts import render

# Create your views here.
def home(request):
    """
    form=ReservationForm()
    if request.method=='POST':
        form.ReservationForm(request.POST)
        if form is is_valid():
            form.save()
    return HttpResponse ('Submision succesfull')
    """
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


# Add your code here to create new views
def menu_view(request):
    menu_items = Menu.objects.all()  # Obtener todos los elementos del menú
    return render(request, 'menu.html', {'menu_items': menu_items})



#aca comienzan los cambios
# blog/views.py


def lista_posts(request):
    posts = Post.objects.filter(publicado=True)
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalle_post(request, pk):
    post = Post.objects.get(pk=pk, publicado=True)
    return render(request, 'blog/detalle_post.html', {'post': post})
