from django.db import models
from django.utils import timezone

class Cupon(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=20, blank=True, null=True)
    imagen = models.ImageField(upload_to='cupones_img/')
    fecha_expiracion = models.DateTimeField()
    activo = models.BooleanField(default=True) # Para activar/desactivar manualmente
    
    # Campo para saber si ya se usó (en este MVP es global)
    fue_canjeado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
    # Una pequeña ayuda para saber si venció
    @property
    def esta_vencido(self):
        return timezone.now() > self.fecha_expiracion