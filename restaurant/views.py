# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from .forms import ReservationForm
#change
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404, render

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

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu_view(request):
    menu_items = Menu.objects.all()  # Obtener todos los elementos del menú
    return render(request, 'menu.html', {'menu_items': menu_items})



#aca comienzan los cambios


def blog(request):
    posts = Post.objects.all()  # Obtiene todas las publicaciones del blog
    return render(request, 'blog.html', {'posts': posts})



def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
