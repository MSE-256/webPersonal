from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   pedido = models.CharField(max_length=250)
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)


class Reservation(models.Model):
   first_name=models.CharField(max_length=255)
   last_name=models.CharField(max_length=255)
   pedido=models.CharField(max_length=500)
   correo=models.CharField(max_length=255)
   comment=models.CharField(max_length=1000)
    

#aca comienzan los cambios
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    excerpt = models.TextField()  # Extracto que se muestra en la página principal
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']  # Ordena por fecha descendente
