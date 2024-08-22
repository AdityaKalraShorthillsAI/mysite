# from rest_framework import viewsets
# from .models import DemographicDataTest
# from rest_framework.pagination import LimitOffsetPagination
# from .const import *
# from .serializer import DemographicDataTestSerializer

# class CustomPagination(LimitOffsetPagination):
#     default_limit = PAGINATION_DEFAULT_LIMIT
#     limit_query_param = PAGINATION_LIMIT_QUERY_PARAM
#     offset_query_param = PAGINATION_OFFSET_QUERY_PARAM

# class DemographicDataTestViewSet(viewsets.ModelViewSet):
#     pagination_class = CustomPagination
#     queryset = DemographicDataTest.objects.all()
#     serializer_class = DemographicDataTestSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from .models import (
    WorkClass,
    Education,
    Occupation,
    MaritalStatus,
    NativeCountry,
    Race,
    Sex,
    Relationship,
    DemographicData,
)
from .serializers import (
    WorkClassSerializer,
    EducationSerializer,
    OccupationSerializer,
    MaritalStatusSerializer,
    NativeCountrySerializer,
    RaceSerializer,
    SexSerializer,
    RelationshipSerializer,
    DemographicDataSerializer,
)
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class WorkClassAPIView(APIView):
    def get(self, request, pk=None):
        cache_key = f"workclass_{pk}" if pk else "all_workclasses"
        data = cache.get(cache_key)

        if not data:
            if pk:
                workclass = get_object_or_404(WorkClass, pk=pk)
                serializer = WorkClassSerializer(workclass)
                data = serializer.data
            else:
                workclasses = WorkClass.objects.all()
                serializer = WorkClassSerializer(workclasses, many=True)
                data = serializer.data
            cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 minutes

        return Response(data)

    def post(self, request):
        serializer = WorkClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        workclass = get_object_or_404(WorkClass, pk=pk)
        serializer = WorkClassSerializer(workclass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f"workclass_{pk}"
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        workclass = get_object_or_404(WorkClass, pk=pk)
        workclass.delete()
        cache_key = f"workclass_{pk}"
        cache.delete(cache_key)
        cache.clear()  # Clear all cache
        return Response(status=status.HTTP_204_NO_CONTENT)


class EducationAPIView(APIView):
    def get(self, request, pk=None):
        cache_key = f"education_{pk}" if pk else "all_education"
        data = cache.get(cache_key)

        if not data:
            if pk:
                education = get_object_or_404(Education, pk=pk)
                serializer = EducationSerializer(education)
                data = serializer.data
            else:
                education = Education.objects.all()
                serializer = EducationSerializer(education, many=True)
                data = serializer.data
            cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 minutes

        return Response(data)

    def post(self, request):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        education = get_object_or_404(Education, pk=pk)
        serializer = EducationSerializer(education, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f"education_{pk}"
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        education = get_object_or_404(Education, pk=pk)
        education.delete()
        cache_key = f"education_{pk}"
        cache.delete(cache_key)
        cache.clear()  # Clear all cache
        return Response(status=status.HTTP_204_NO_CONTENT)


class OccupationAPIView(APIView):
    def get(self, request, pk=None):
        cache_key = f"occupation_{pk}" if pk else "all_occupation"
        data = cache.get(cache_key)

        if not data:
            if pk:
                occupation = get_object_or_404(Occupation, pk=pk)
                serializer = OccupationSerializer(occupation)
                data = serializer.data
            else:
                occupation = Occupation.objects.all()
                serializer = OccupationSerializer(occupation, many=True)
                data = serializer.data
            cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 minutes

        return Response(data)

    def post(self, request):
        serializer = OccupationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        occupation = get_object_or_404(Occupation, pk=pk)
        serializer = OccupationSerializer(occupation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f"occupation_{pk}"
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        occupation = get_object_or_404(Occupation, pk=pk)
        occupation.delete()
        cache_key = f"occupation_{pk}"
        cache.delete(cache_key)
        cache.clear()  # Clear all cache
        return Response(status=status.HTTP_204_NO_CONTENT)


class MaritalStatusAPIView(APIView):
    def get(self, request, pk=None):
        cache_key = f"maritalstatus_{pk}" if pk else "all_maritalstatuses"
        data = cache.get(cache_key)

        if not data:
            if pk:
                maritalstatus = get_object_or_404(MaritalStatus, pk=pk)
                serializer = MaritalStatusSerializer(maritalstatus)
                data = serializer.data
            else:
                maritalstatus = MaritalStatus.objects.all()
                serializer = MaritalStatusSerializer(maritalstatus, many=True)
                data = serializer.data
            cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 minutes

        return Response(data)

    def post(self, request):
        serializer = MaritalStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        maritalstatus = get_object_or_404(MaritalStatus, pk=pk)
        serializer = MaritalStatusSerializer(maritalstatus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f"maritalstatus_{pk}"
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        maritalstatus = get_object_or_404(MaritalStatus, pk=pk)
        maritalstatus.delete()
        cache_key = f"maritalstatus_{pk}"
        cache.delete(cache_key)
        cache.clear()  # Clear all cache
        return Response(status=status.HTTP_204_NO_CONTENT)


class NativeCountryAPIView(APIView):
    def get(self, request, pk=None):
        cache_key = f"nativecountry_{pk}" if pk else "all_nativecountries"
        data = cache.get(cache_key)

        if not data:
            if pk:
                nativecountry = get_object_or_404(NativeCountry, pk=pk)
                serializer = NativeCountrySerializer(nativecountry)
                data = serializer.data
            else:
                nativecountry = NativeCountry.objects.all()
                serializer = NativeCountrySerializer(nativecountry, many=True)
                data = serializer.data
            cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 minutes

        return Response(data)

    def post(self, request):
        serializer = NativeCountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        nativecountry = get_object_or_404(NativeCountry, pk=pk)
        serializer = NativeCountrySerializer(nativecountry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f"nativecountry_{pk}"
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        nativecountry = get_object_or_404(NativeCountry, pk=pk)
        nativecountry.delete()
        cache_key = f"nativecountry_{pk}"
        cache.delete(cache_key)
        cache.clear()  # Clear all cache
        return Response(status=status.HTTP_204_NO_CONTENT)


class RaceAPIView(APIView):
    def get(self, request, pk=None):
        cache_key = f"race_{pk}" if pk else "all_races"
        data = cache.get(cache_key)

        if not data:
            if pk:
                race = get_object_or_404(Race, pk=pk)
                serializer = RaceSerializer(race)
                data = serializer.data
            else:
                races = Race.objects.all()
                serializer = RaceSerializer(races, many=True)
                data = serializer.data
            cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 minutes

        return Response(data)

    def post(self, request):
        serializer = RaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        race = get_object_or_404(Race, pk=pk)
        serializer = RaceSerializer(race, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f"race_{pk}"
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        race = get_object_or_404(Race, pk=pk)
        race.delete()
        cache_key = f"race_{pk}"
        cache.delete(cache_key)
        cache.clear()  # Clear all cache
        return Response(status=status.HTTP_204_NO_CONTENT)


class SexAPIView(APIView):
    def get(self, request, pk=None):
        cache_key = f"sex_{pk}" if pk else "all_sex"
        data = cache.get(cache_key)

        if not data:
            if pk:
                sex = get_object_or_404(Sex, pk=pk)
                serializer = SexSerializer(sex)
                data = serializer.data
            else:
                sex = Sex.objects.all()
                serializer = SexSerializer(sex, many=True)
                data = serializer.data
            cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 minutes

        return Response(data)

    def post(self, request):
        serializer = SexSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        sex = get_object_or_404(Sex, pk=pk)
        serializer = SexSerializer(sex, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f"sex_{pk}"
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sex = get_object_or_404(Sex, pk=pk)
        sex.delete()
        cache_key = f"sex_{pk}"
        cache.delete(cache_key)
        cache.clear()  # Clear all cache
        return Response(status=status.HTTP_204_NO_CONTENT)


class RelationshipAPIView(APIView):
    def get(self, request, pk=None):
        cache_key = f"relationship_{pk}" if pk else "all_relationships"
        data = cache.get(cache_key)

        if not data:
            if pk:
                relationship = get_object_or_404(Relationship, pk=pk)
                serializer = RelationshipSerializer(relationship)
                data = serializer.data
            else:
                relationship = Relationship.objects.all()
                serializer = RelationshipSerializer(relationship, many=True)
                data = serializer.data
            cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 minutes

        return Response(data)

    def post(self, request):
        serializer = RelationshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        relationship = get_object_or_404(Relationship, pk=pk)
        serializer = RelationshipSerializer(relationship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f"relationship_{pk}"
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        relationship = get_object_or_404(Relationship, pk=pk)
        relationship.delete()
        cache_key = f"relationship_{pk}"
        cache.delete(cache_key)
        cache.clear()  # Clear all cache
        return Response(status=status.HTTP_204_NO_CONTENT)


class DemographicDataAPIView(APIView):
    def get(self, request, pk=None):

        cache_key = (
            f"demographicdata_{pk}"
            if pk
            else f"all_demographicdata_{request.GET.get('p_num', 1)}__{request.GET.get('p_size', 10)}"
        )
        data = cache.get(cache_key)

        if not data:
            queryset = DemographicData.objects.select_related(
                "workclass",
                "occupation",
                "sex",
                "race",
                "marital_status",
                "education",
                "relationship",
                "native_country",
            ).all()
            if pk:
                demographic_data = get_object_or_404(
                    queryset,
                    pk=pk,
                )
                serializer = DemographicDataSerializer(demographic_data)
                data = serializer.data
            else:
                page_number = request.GET.get("p_num", 1)
                page_size = request.GET.get("p_size", 10)
                paginator = Paginator(queryset, page_size)

                try:
                    page_posts = paginator.page(page_number)
                except PageNotAnInteger:
                    page_posts = paginator.page(1)
                except EmptyPage:
                    page_posts = paginator.page(paginator.num_pages)

                serializer = DemographicDataSerializer(page_posts, many=True)
                data = serializer.data
            cache.set(cache_key, data, timeout=60 * 15)

        return Response(data)

    def post(self, request):
        serializer = DemographicDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        demographic_data = get_object_or_404(DemographicData, pk=pk)
        serializer = DemographicDataSerializer(demographic_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f"demographicdata_{pk}"
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        demographic_data = get_object_or_404(DemographicData, pk=pk)
        demographic_data.delete()
        cache_key = f"demographicdata_{pk}"
        cache.delete(cache_key)
        cache.clear()  # Clear all cache
        return Response(status=status.HTTP_204_NO_CONTENT)
