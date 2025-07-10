# from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu, Post, Market
#change
from django.shortcuts import render
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
    post_items = Post.objects.all()  # Obtener todos los elementos del menú
    return render(request, 'lista_posts.html', {'post_items': post_items})

def market(request):
    market_items = Market.objects.all()  # Obtener todos los elementos del menú
    return render(request, 'marketplace.html', {'market_items': market_items})

def mole_view(request):
    mole_items = Menu.objects.all()  # Obtener todos los elementos del menú
    return render(request, 'lamole.html', {'mole_items': mole_items})

def business_view(request):
    business_items = Menu.objects.all()  # Obtener todos los elementos del menú
    return render(request, 'emprendedorismo.html', {'business_items': business_items})

def holmes_view(request):
    holmes_items = Menu.objects.all()  # Obtener todos los elementos del menú
    return render(request, 'investigaciones.html', {'holmes_items': holmes_items})

def academy_view(request):
    academy_items = Menu.objects.all()  # Obtener todos los elementos del menú
    return render(request, 'academy.html', {'academy_items': academy_items})