from rest_framework import viewsets
from .models import DemographicDataTest
from rest_framework.pagination import LimitOffsetPagination
from .const import *
from .serialiser import DemographicDataTestSerializer

class CustomPagination(LimitOffsetPagination):
    default_limit = PAGINATION_DEFAULT_LIMIT
    limit_query_param = PAGINATION_LIMIT_QUERY_PARAM
    offset_query_param = PAGINATION_OFFSET_QUERY_PARAM

class DemographicDataTestViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination
    queryset = DemographicDataTest.objects.all()
    serializer_class = DemographicDataTestSerializer
