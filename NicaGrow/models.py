from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _


class UsuarioManager(BaseUserManager):

    def create_user(self, correo, password=None, tipo=None, **extra_fields):
        if not correo:
            raise ValueError("El correo es obligatorio")
        correo = self.normalize_email(correo)
        usuario = self.model(correo=correo, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")
        return self.create_user(correo, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    Id = models.BigAutoField(primary_key=True)
    correo = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "correo"
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    class Meta:
        db_table = "Usuario"

    def __str__(self):
        return self.correo

class Ciudad(models.Model):
    Id = models.CharField(max_length=50, null=False, primary_key=True)
    Ciudad = models.CharField(max_length=50, null=False, unique=True)

class Categoria(models.Model):
    Id = models.AutoField(primary_key=True)
    Categoria = models.CharField(max_length=50, null=False, unique=True)

class Estado(models.Model):
    Id = models.AutoField(primary_key=True)
    Tipo_Estado = models.CharField(max_length=50, unique=True, null=False)

class MetodoPago(models.Model):
    Id = models.AutoField(primary_key=True)
    Metodo = models.CharField(max_length=50, unique=True, null=False)

class MetodoEnvio(models.Model):
    Id = models.AutoField(primary_key=True)
    MetodoEnvio = models.CharField(max_length=50, unique=True, null=False)

class Cliente(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=50, null=False)
    Apellidos = models.CharField(max_length=50, null=False)
    Email = models.EmailField(unique=True, null=False)
    Telefono = models.CharField(
        max_length=8,
        unique=True,
        validators=[MinValueValidator(10000000), MaxValueValidator(99999999)]
    )
    FNacimiento = models.DateField(null=False)
    IdCiudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)

class Vendedor(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=50, null=False)
    Apellidos = models.CharField(max_length=50, null=False)
    NombreNegocio= models.CharField(max_length=50, null=False)
    Email = models.EmailField(unique=True, null=False)
    Telefono = models.CharField(
        max_length=8,
        unique=True,
        validators=[MinValueValidator(10000000), MaxValueValidator(99999999)]
    )
    FNacimiento = models.DateField(null=False)
    IdCiudad= models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)

class Producto(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50, null=False)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    IdVendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    IdCategoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

class Venta(models.Model):
    Id = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=100, null=False)
    Cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    IdVendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    IdProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    IdEstado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)

class Pedido(models.Model):
    Id = models.AutoField(primary_key=True)
    FechaPedido = models.DateField(null=False)
    Total = models.DecimalField(
        validators=[MinValueValidator(0)], max_digits=10, decimal_places=2
    )
    IdCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    IdMetodoPago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True)
    IdMetodoEnvio = models.ForeignKey(MetodoEnvio, on_delete=models.SET_NULL, null=True)
    IdEstado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)

class DetallePedido(models.Model):
    Id = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    IdProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    IdPedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)

class HistorialBusqueda(models.Model):
    Id = models.AutoField(primary_key=True)
    Busqueda = models.CharField(max_length=255)
    FechaBusqueda = models.DateTimeField(null=False)
    IdCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

class Reseña(models.Model):
    Id = models.AutoField(primary_key=True)
    Calificacion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    Descripcion = models.CharField(max_length=255, null=True)
    Fecha = models.DateTimeField(null=False)
    IdCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    IdProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)

class CredencialCliente(models.Model):
    id_Usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class CredencialVendedor(models.Model):
    id_Usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    id_Vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

