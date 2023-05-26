from rest_framework import serializers
from .models import *
from service.serializers import ServiceCompanySerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class EngineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineModel
        fields = '__all__'

class TransmissionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionModel
        fields = '__all__'

class DriveAxleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveAxleModel
        fields = '__all__'

class SteerableAxleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteerableAxleModel
        fields = '__all__'


class AutoCarSerializer(serializers.ModelSerializer):
    car_model = CarModelSerializer()
    engine_model = EngineModelSerializer()
    transmission_model = TransmissionModelSerializer()
    drive_axle_model = DriveAxleModelSerializer()
    steerable_axle_model = SteerableAxleModelSerializer()
    service_company = ServiceCompanySerializer()
    client = UserSerializer()
    class Meta:
        model = AutoCar
        fields = '__all__'