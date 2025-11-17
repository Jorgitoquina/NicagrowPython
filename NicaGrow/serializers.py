from rest_framework import serializers
from .models import Cliente
from .models import Categoria
from .models import Ciudad
from .models import CredencialCliente
from .models import CredencialVendedor
from .models import DetallePedido
from .models import Estado
from .models import HistorialBusqueda
from .models import MetodoEnvio
from .models import MetodoPago
from .models import Pedido
from .models import Producto
from .models import Reseña
from .models import Usuario
from .models import Vendedor
from .models import Venta


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['Id', 'correo', 'is_active', 'is_staff']
        read_only_fields = ['Id', 'is_active', 'is_staff']

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['correo', 'password']

    def create(self, validated_data):
        return Usuario.objects.create_user(
            correo=validated_data['correo'],
            password=validated_data['password']
        )

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['Id', 'Ciudad']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['Id', 'Nombres', 'Apellidos', 'Email', 'Telefono', 'FNacimiento', 'IdCiudad']
        read_only_fields = ['Id']

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['Id', 'Nombres', 'Apellidos', 'Email', 'Telefono', 'FNacimiento', 'IdCiudad']
        read_only_fields = ['Id']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['Id', 'Categoria']
        read_only_fields = ['Id']


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['Id', 'Tipo_Estado']
        read_only_fields = ['Id']

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['Id', 'Metodo']
        read_only_fields = ['Id']

class MetodoEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoEnvio
        fields = ['Id', 'MetodoEnvio']
        read_only_fields = ['Id']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['Id', 'Nombre', 'Precio', 'IdVendedor', 'IdCategoria']
        read_only_fields = ['Id']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['Id', 'Descripcion', 'Cantidad', 'IdVendedor', 'IdProducto', 'IdEstado']
        read_only_fields = ['Id']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['Id', 'FechaPedido', 'Total', 'IdCliente', 'IdMetodoPago', 'IdMetodoEnvio', 'IdEstado']
        read_only_fields = ['Id']

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['Id', 'Cantidad', 'IdProducto', 'IdPedido']
        read_only_fields = ['Id']

class HistorialBusquedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialBusqueda
        fields = ['Id', 'Busqueda', 'FechaBusqueda', 'IdCliente']
        read_only_fields = ['Id']

class ReseñaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseña
        fields = ['Id', 'Calificacion', 'Descripcion', 'Fecha', 'IdCliente', 'IdProducto']
        read_only_fields = ['Id']

class CredencialClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CredencialCliente
        fields = ['id_Usuario', 'id_Cliente']

class CredencialVendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CredencialVendedor
        fields = ['id_Usuario', 'id_Vendedor']