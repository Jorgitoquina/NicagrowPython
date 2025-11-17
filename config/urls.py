from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from NicaGrow.views import (
    UsuarioViewSet,
    CiudadViewSet,
    CategoriaViewSet,
    EstadoViewSet,
    MetodoPagoViewSet,
    MetodoEnvioViewSet,
    ClienteViewSet,
    VendedorViewSet,
    ProductoViewSet,
    VentaViewSet,
    PedidoViewSet,
    DetallePedidoViewSet,
    HistorialBusquedaViewSet,
    ReseñaViewSet,
    CredencialClienteViewSet,
    CredencialVendedorViewSet,
)

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet, basename="usuario")
router.register(r"ciudades", CiudadViewSet, basename="ciudad")
router.register(r"categorias", CategoriaViewSet)
router.register(r"estados", EstadoViewSet)
router.register(r"metodos-pago", MetodoPagoViewSet)
router.register(r"metodos-envio", MetodoEnvioViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"vendedores", VendedorViewSet)
router.register(r"productos", ProductoViewSet)
router.register(r"ventas", VentaViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles-pedido', DetallePedidoViewSet)
router.register(r'historial-busqueda', HistorialBusquedaViewSet)
router.register(r'reseñas', ReseñaViewSet)
router.register(r'credenciales-cliente', CredencialClienteViewSet)
router.register(r'credenciales-vendedor', CredencialVendedorViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
