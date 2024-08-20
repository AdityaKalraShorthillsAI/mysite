from .views import *
from rest_framework.routers import DefaultRouter
from .views import DemographicDataTestViewSet

router = DefaultRouter()
router.register(r'demographic_data', DemographicDataTestViewSet, basename='dataset')


urlpatterns = router.urls