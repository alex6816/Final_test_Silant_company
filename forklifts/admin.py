from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
from import_export import resources
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserInline(admin.StackedInline):
    model = UserAcc
    can_delete = False
    verbose_name_plural = 'Дополнительная информация'
 
# Для модели User устанавливаем новый класс настроек
class UserAdmin(UserAdmin):
    inlines = (UserInline, )
 
# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Модель погрузчика
class CarModelResource(resources.ModelResource):
    class Meta:
        model = CarModel
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(CarModel)
class CarModelAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = CarModelResource
    list_display = ('id','name','description',)
    filter = ('name',)


# Модель двигателя
class EngineResource(resources.ModelResource):
    class Meta:
        model = EngineModel
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(EngineModel)
class EngineAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = EngineResource
    list_display = ('id','name','description',)
    filter = ('name',)


# Модель трансмиссии
class TransmissionResource(resources.ModelResource):
    class Meta:
        model = TransmissionModel
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(TransmissionModel)
class TransmissionAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = TransmissionResource
    list_display = ('id','name','description',)
    filter = ('name',)


# Модель ведущего моста
class DriveAxleResource(resources.ModelResource):
    class Meta:
        model = DriveAxleModel
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(DriveAxleModel)
class DrivingBridgeAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = DriveAxleResource
    list_display = ('id','name','description',)
    filter = ('name',)


# Модель управляемого моста
class SteerableAxleResource(resources.ModelResource):
    class Meta:
        model = SteerableAxleModel
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(SteerableAxleModel)
class ControlledBridgeAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = SteerableAxleResource
    list_display = ('id','name','description',)
    filter = ('name',)


# Погрузчики
class AutoCarResource(resources.ModelResource):
    class Meta:
        model = AutoCar
        report_skipped = True
        fields = (
        'id',
        'serial_number',
        'car_model',
        'engine_model',
        'engine_number',
        'transmission_model',
        'transmission_number',
        'drive_axle_model',
        'drive_axle_number',
        'steerable_axle_model',
        'steerable_axle_number',
        'supply_contract',
        'shipment_date',
        'consumer',
        'delivery_address',
        'equipment',
        'client',
        'service_company',
        )

@admin.register(AutoCar)
class CarAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = AutoCarResource
    list_display = (
        'id',
        'serial_number',
        'car_model',        
        'engine_model',
        'transmission_model',
        'drive_axle_model',
        'steerable_axle_model',
        'shipment_date',
        'equipment',
        'client',
        'service_company',
    )
    filter = ('serial_number',)   
