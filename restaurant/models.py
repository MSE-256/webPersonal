from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField()
   price = models.DecimalField(max_digits=6, decimal_places=2)

   def __str__(self):
      return self.name

class Reservation(models.Model):
   first_name=models.CharField(max_length=255)
   last_name=models.CharField(max_length=255)
   guest_count=models.IntegerField()
   reservation_time=models.DateField(auto_now=True)
   comment=models.CharField(max_length=1000)
    
    