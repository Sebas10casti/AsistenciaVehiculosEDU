from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, RegistroViewSet

router = DefaultRouter()
router.register(r'vehicles', VehiculoViewSet, basename='vehicle')
router.register(r'registros', RegistroViewSet, basename='registro')

urlpatterns = router.urls
