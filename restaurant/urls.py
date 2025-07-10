from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu_view, name='menu'),
    path('lamole/', views.mole_view, name='lamole'),
    path('emprendedorismo/', views.business_view, name='emprendedorismo'),
    path('investigaciones/', views.holmes_view, name='investigaciones'),
    path('academy/', views.academy_view, name='academy'),
    path('marketplace/', views.market, name='marketplace'),
    path('lista_posts', views.lista_posts, name='lista_posts'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

