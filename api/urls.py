from rest_framework.routers import DefaultRouter
from api.views import FundoImobiliĆ”rioViewSet


app_name = "api"

router = DefaultRouter()
router.register(r"fundos", FundoImobiliĆ”rioViewSet)

urlpatterns = router.urls
