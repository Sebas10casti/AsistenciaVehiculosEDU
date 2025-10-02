from django.db import models

class Vehiculo(models.Model):
    TIPO_CHOICES = (
        ('carro', 'Carro'),
        ('moto', 'Moto'),
        ('bicicleta', 'Bicicleta'),
    )
    AREA_CHOICES = (
        ('produccion', 'Producción'),
        ('administracion', 'Administración'),
        ('logistica', 'Logística'),
        ('soplado', 'Soplado'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nombre_dueno = models.CharField("Nombre del dueño", max_length=150)
    documento = models.CharField("Documento", max_length=50)
    placa = models.CharField("Placa", max_length=30, blank=True, null=True)
    color = models.CharField("Color", max_length=50)
    marca = models.CharField("Marca", max_length=80, blank=True, null=True)
    area = models.CharField("Área", max_length=30, choices=AREA_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        iden = self.placa or ""
        return f"{self.nombre_dueno} - {self.tipo} ({iden})"


class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, related_name='registros', on_delete=models.CASCADE)
    placa = models.CharField("Placa", max_length=80, help_text="Placa del vehículo", default="")
    fecha = models.DateField(auto_now_add=True)           # fecha del ingreso (día)
    hora_entrada = models.DateTimeField(auto_now_add=True) # timestamp de entrada
    hora_salida = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-hora_entrada']

    def __str__(self):
        return f"{self.placa} - {self.fecha} - entrada:{self.hora_entrada} salida:{self.hora_salida}"
