# from .views import *
# from rest_framework.routers import DefaultRouter
# from .views import DemographicDataTestViewSet

# # router = DefaultRouter()
# # router.register(r'demographic_data', DemographicDataTestViewSet, basename='dataset')


# urlpatterns = router.urls
from django.urls import path
from django.conf import settings
from .views import WorkClassAPIView, EducationAPIView, OccupationAPIView, MaritalStatusAPIView, NativeCountryAPIView, RaceAPIView, SexAPIView, RelationshipAPIView, DemographicDataAPIView

urlpatterns = [
    path('workclass/', WorkClassAPIView.as_view()),
    path('workclass/<int:pk>/', WorkClassAPIView.as_view()),
    path('education/', EducationAPIView.as_view()),
    path('education/<int:pk>/', EducationAPIView.as_view()),
    path('occupation/', OccupationAPIView.as_view()),
    path('occupation/<int:pk>/', OccupationAPIView.as_view()),
    path('maritalstatus/', MaritalStatusAPIView.as_view()),
    path('maritalstatus/<int:pk>/', MaritalStatusAPIView.as_view()),
    path('nativecountry/', NativeCountryAPIView.as_view()),
    path('nativecountry/<int:pk>/', NativeCountryAPIView.as_view()),
    path('race/', RaceAPIView.as_view()),
    path('race/<int:pk>/', RaceAPIView.as_view()),
    path('sex/', SexAPIView.as_view()),
    path('sex/<int:pk>/', SexAPIView.as_view()),
    path('relationship/', RelationshipAPIView.as_view()),
    path('relationship/<int:pk>/', RelationshipAPIView.as_view()),
    path('demographicdata/', DemographicDataAPIView.as_view()),
    path('demographicdata/<int:pk>/', DemographicDataAPIView.as_view()),
]


# urls.py



# if settings.DEBUG:

# from django.urls import path
# from .views import DemographicDataListCreateView, DemographicDataRetrieveView

# urlpatterns = [
#     path('demographicdata/', DemographicDataListCreateView.as_view(), name='demographicdata-list-create'),
#     path('demographicdata/<int:pk>/', DemographicDataRetrieveView.as_view(), name='demographicdata-retrieve'),
# ]
