from rest_framework import serializers
from .models import Camera, FireSmokeWeaponDetection, AgeGender, FaceRecognition, LicensePlateRecognition, LprAlpha


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'name', 'notes', 'location', 'latitude', 'longitude']


class FireSmokeWeaponDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireSmokeWeaponDetection
        fields = ["camera", "alarm_title", "severity", "status"]


class AgeGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGender
        fields = ["camera", "created_at", "male_kids", "female_kids", "male_teens", "female_teens", "male_adults", "female_adults", "male_old", "female_old"]


class FaceRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceRecognition
        fields = ["camera", "created_at", "image"]


class LicensePlateRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensePlateRecognition
        fields = ["camera", "plate_number", "created_at"]

class LprAlphaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LprAlpha
        fields = ["camera", "plate_number", "confidence_score", "lpr_image", "car_image", "created_at"]

class DateRangeSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
