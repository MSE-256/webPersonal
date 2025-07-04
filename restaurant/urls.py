from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu_view, name='menu'),
    path('book/', views.book, name="book"),
    path('blog/', views.blog, name='blog'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


