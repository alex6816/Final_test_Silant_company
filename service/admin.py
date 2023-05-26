from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
from import_export import resources


# Вид технического обслуживания
class MaintenanceTypeResource(resources.ModelResource):
    class Meta:
        model = MaintenanceType
        report_skipped = True
        fields = ('id','name','description',)


@admin.register(MaintenanceType)
class MaintenanceTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MaintenanceTypeResource
    list_display = ('id','name','description',)
    filter = ('name',) 


# Описание отказа
class FailureNodeResource(resources.ModelResource):
    class Meta:
        model = FailureNode
        report_skipped = True
        fields = ('id','name','description',)  


@admin.register(FailureNode)
class FailureNodeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FailureNodeResource
    list_display = ('id','name','description',)
    filter = ('name',)                 


# Способ восстановления
class RecoveryMethodResource(resources.ModelResource):
    class Meta:
        model = RecoveryMethod
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(RecoveryMethod)
class RecoveryMethodAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = RecoveryMethodResource
    list_display = ('id','name','description',)
    filter = ('name',)


# Сервисная компания
class ServiceCompanyResource(resources.ModelResource):
    class Meta:
        model = ServiceCompany
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(ServiceCompany)
class ServiceCompanyAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ServiceCompanyResource
    list_display = ('id','name','description',)
    filter = ('name',)  


# Техническое обслуживание
class MaintenanceResource(resources.ModelResource):
    class Meta:
        model = Maintenance
        report_skipped = True
        fields = ('id','maintenance_type','maintenance_date','operating_time','work_order_number','work_order_date','service_company','autocar')

@admin.register(Maintenance)
class MaintenanceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MaintenanceResource
    list_display = ('id','maintenance_type','maintenance_date','operating_time','work_order_number','work_order_date','service_company','autocar')
    filter = ('maintenance_date',) 


# Рекламация
class ClaimResource(resources.ModelResource):
    class Meta:
        model = Claim
        report_skipped = True
        fields = ('id','failure_date','operating_time','failure_node','failure_description','recovery_method','spare_parts','recovery_date','downtime','autocar','service_company')

@admin.register(Claim)
class ClaimAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ClaimResource
    list_display = ('id','failure_date','operating_time','failure_node','failure_description','recovery_date','downtime','autocar','service_company')
    filter = ('failure_date',)             