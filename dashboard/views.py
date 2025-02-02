from rest_framework import viewsets
from .models import Camera, FireSmokeWeaponDetection, AgeGender, FaceRecognition, LicensePlateRecognition, LprAlpha
from .serializers import CameraSerializer, FireSmokeWeaponDetectionSerializer, AgeGenderSerializer, FaceRecognitionSerializer, LicensePlateRecognitionSerializer, DateRangeSerializer, LprAlphaSerializer
from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import DefaultPagination



class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class FireSmokeWeaponDetectionViewSet(viewsets.ModelViewSet):
    queryset = FireSmokeWeaponDetection.objects.all()
    serializer_class = FireSmokeWeaponDetectionSerializer


class AgeGenderViewSet(viewsets.ModelViewSet):
    queryset = AgeGender.objects.all().order_by('-created_at')
    serializer_class = AgeGenderSerializer


class FaceRecognitionViewSet(viewsets.ModelViewSet):
    queryset = FaceRecognition.objects.all()
    serializer_class = FaceRecognitionSerializer

    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        camera_id = self.request.query_params.get('camera_id')
        if camera_id:
            queryset = queryset.filter(camera=camera_id)
        queryset = queryset.order_by('-created_at')
        return queryset

class LicensePlateRecognitionViewSet(viewsets.ModelViewSet):
    queryset = LicensePlateRecognition.objects.all()
    serializer_class = LicensePlateRecognitionSerializer

class LprAlphaViewSet(viewsets.ModelViewSet):
    queryset = LprAlpha.objects.all()
    serializer_class = LprAlphaSerializer

    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        camera_id = self.request.query_params.get('camera_id')
        # date = self.request.query_params.get('date')
        if camera_id:
            queryset = queryset.filter(camera=camera_id)
        # if date:
        #     queryset = queryset.filter(created_at__date > date)
        queryset = queryset.order_by('-created_at')
        return queryset


    
class AgeGenderSummaryView(APIView):
    def get(self, request):
        serializer = DateRangeSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        # Query AgeGender table for records within the date range and aggregate sums
        age_gender_summary = AgeGender.objects.filter(created_at__range=(start_date, end_date)).aggregate(
            sum_male_kids=Sum('male_kids'),
            sum_female_kids=Sum('female_kids'),
            sum_male_teens=Sum('male_teens'),
            sum_female_teens=Sum('female_teens'),
            sum_male_adults=Sum('male_adults'),
            sum_female_adults=Sum('female_adults'),
            sum_male_old=Sum('male_old'),
            sum_female_old=Sum('female_old')
        )

        return Response(age_gender_summary, status=status.HTTP_200_OK)

class AgeGenderCountView(APIView):
    serializer_class = AgeGenderSerializer

    def get(self, request):
        # Retrieve the last record from the AgeGender table
        last_record = AgeGender.objects.last()

        if last_record:
            serializer = self.serializer_class(last_record)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No records found'}, status=status.HTTP_404_NOT_FOUND)