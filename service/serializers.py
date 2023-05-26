from rest_framework import serializers
from .models import *



class ServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = '__all__'

class MaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceType
        fields = '__all__'

class FailureNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureNode
        fields = '__all__'

class RecoveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryMethod
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    maintenance_type = MaintenanceTypeSerializer()
    service_company = ServiceCompanySerializer()
    class Meta:
        model = Maintenance
        fields = '__all__'

class ClaimSerializer(serializers.ModelSerializer):
    failure_node = FailureNodeSerializer()
    recovery_method = RecoveryMethodSerializer()
    service_company = ServiceCompanySerializer()
    class Meta:
        model = Claim
        fields = '__all__'
        