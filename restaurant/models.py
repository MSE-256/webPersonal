from django.db import models
from django.contrib.auth.models import User

# Add code to create Menu model
class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    contenido = models.TextField(max_length=200)


#aca comienzan los cambios
# blog/models.py

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Market(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField()
    price=models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Mole(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField()
    price=models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Holmes(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Business(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.title

class Academy(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.title