from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class UserAcc(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_service = models.BooleanField(default=False, blank=True, verbose_name='Сотрудник сервисной компании')
    service_company = models.ForeignKey(to='service.ServiceCompany', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.user.username} {self.is_service}'
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class AutoCar(models.Model):
    serial_number = models.CharField(max_length=16, unique=True, verbose_name='Заводской номер погрузчика')
    car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE, verbose_name='Модель техники')        
    engine_model = models.ForeignKey('EngineModel', on_delete=models.CASCADE, verbose_name='Модель двигателя')
    engine_number = models.CharField(max_length=16, verbose_name='Заводской номер двигателя')
    transmission_model = models.ForeignKey('TransmissionModel', on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    transmission_number = models.CharField(max_length=16, verbose_name='Заводской номер трансмиссии')
    drive_axle_model = models.ForeignKey('DriveAxleModel', on_delete=models.CASCADE, verbose_name='Модель ведущего моста')
    drive_axle_number = models.CharField(max_length=16, verbose_name='Заводской номер ведущего моста')
    steerable_axle_model = models.ForeignKey('SteerableAxleModel', on_delete=models.CASCADE, verbose_name='Модель управляемого моста')
    steerable_axle_number = models.CharField(max_length=16, verbose_name='Заводской номер управляемого моста')
    supply_contract = models.CharField(max_length=32, verbose_name='Договор поставки №, дата')
    shipment_date = models.DateField(default=datetime.now, verbose_name='Дата отгрузки с завода')
    consumer = models.CharField(max_length=128, verbose_name='Грузополучатель (конечный потребитель)')
    delivery_address = models.CharField(max_length=256, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(blank=False, verbose_name='Комплектация (доп. опции)', default="Стандарт")
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    service_company = models.ForeignKey(to='service.ServiceCompany', on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.serial_number}'

    class Meta:
        verbose_name = 'Погрузчик'
        verbose_name_plural = 'Погрузчики'

# Справочники

class CarModel(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники' 

class EngineModel(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей' 

class TransmissionModel(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'  

class DriveAxleModel(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущих мостов' 

class SteerableAxleModel(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемых мостов'    
                                       