from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    Usuario,
    Ciudad,
    Categoria,
    Estado,
    MetodoPago,
    MetodoEnvio,
    Cliente,
    Vendedor,
    Producto,
    Venta,
    Pedido,
    DetallePedido,
    HistorialBusqueda,
    Reseña,
    CredencialCliente,
    CredencialVendedor,
)
from .serializers import (
    UsuarioSerializer,
    CiudadSerializer,
    CategoriaSerializer,
    EstadoSerializer,
    MetodoPagoSerializer,
    MetodoEnvioSerializer,
    ClienteSerializer,
    VendedorSerializer,
    ProductoSerializer,
    VentaSerializer,
    PedidoSerializer,
    DetallePedidoSerializer,
    HistorialBusquedaSerializer,
    ReseñaSerializer,
    CredencialClienteSerializer,
    CredencialVendedorSerializer,
)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    correo = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        correo = attrs.get("correo")
        password = attrs.get("password")

        try:
            user = Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("No existe una cuenta con ese correo")

        if not user.check_password(password):
            raise serializers.ValidationError("Contraseña incorrecta")

        if not user.is_active:
            raise serializers.ValidationError("La cuenta está inactiva")

        refresh = self.get_token(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

User = get_user_model()

class UsuarioViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class CiudadViewSet(ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = [IsAuthenticated]

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = [IsAuthenticated]

class MetodoPagoViewSet(ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
    permission_classes = [IsAuthenticated]

class MetodoEnvioViewSet(ModelViewSet):
    queryset = MetodoEnvio.objects.all()
    serializer_class = MetodoEnvioSerializer
    permission_classes = [IsAuthenticated]

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]


class VendedorViewSet(ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    permission_classes = [IsAuthenticated]

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class VentaViewSet(ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

class DetallePedidoViewSet(ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    permission_classes = [IsAuthenticated]

class HistorialBusquedaViewSet(ModelViewSet):
    queryset = HistorialBusqueda.objects.all()
    serializer_class = HistorialBusquedaSerializer
    permission_classes = [IsAuthenticated]

class ReseñaViewSet(ModelViewSet):
    queryset = Reseña.objects.all()
    serializer_class = ReseñaSerializer
    permission_classes = [IsAuthenticated]

class CredencialClienteViewSet(ModelViewSet):
    queryset = CredencialCliente.objects.all()
    serializer_class = CredencialClienteSerializer
    permission_classes = [IsAuthenticated]

class CredencialVendedorViewSet(ModelViewSet):
    queryset = CredencialVendedor.objects.all()
    serializer_class = CredencialVendedorSerializer
    permission_classes = [IsAuthenticated]

