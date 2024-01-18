from django.db import models

class Producto(models.Model):
    nombre= models.CharField(max_length= 50, null=False, blank=False, verbose_name='nombre')
    precio= models.DecimalField(max_digits=6, decimal_places= 2, null= False, blank= False, verbose_name='precio')
    cantidad = models.IntegerField(null= False, blank= False, verbose_name= 'cantidad')
    objects = models.Manager()

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'
        db_table= 'producto'


    def __str__(self):
        data = "{0} {1} {2}"
        return data.format(self.nombre, self.precio, self.cantidad)