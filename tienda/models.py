from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='tienda')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='tienda'
        verbose_name_plural='tiendas'

    def __str__(self):
        return self.titulo