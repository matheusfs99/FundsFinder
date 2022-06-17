from rest_framework.routers import DefaultRouter
from api.views import FundoImobiliárioViewSet


app_name = "api"

router = DefaultRouter()
router.register(r"fundos", FundoImobiliárioViewSet)

urlpatterns = router.urls
