from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Marcas"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorias"


class Reloj(models.Model):
    GENERO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('U', 'Unisex'),
    ]
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='relojes')
    modelo = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default='U')
    descripcion = models.TextField(blank=True)
    imagen_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.marca} - {self.modelo}"

    class Meta:
        verbose_name_plural = "Relojes"


class RelojCategoria(models.Model):
    reloj = models.ForeignKey(Reloj, on_delete=models.CASCADE, related_name='categorias')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='relojes')

    def __str__(self):
        return f"{self.reloj} - {self.categoria}"

    class Meta:
        verbose_name_plural = "Reloj Categorias"
        unique_together = ('reloj', 'categoria')


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Clientes"


class PerfilCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='perfil')
    fecha_nacimiento = models.DateField(blank=True, null=True)
    documento_identidad = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Perfil de {self.cliente}"

    class Meta:
        verbose_name_plural = "Perfiles de Cliente"


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Venta #{self.id} - {self.cliente}"

    class Meta:
        verbose_name_plural = "Ventas"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    reloj = models.ForeignKey(Reloj, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.venta} - {self.reloj}"

    class Meta:
        verbose_name_plural = "Detalles de Venta"