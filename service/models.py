from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from forklifts.models import AutoCar, UserAcc


class Maintenance(models.Model):
    maintenance_type = models.ForeignKey('MaintenanceType', on_delete=models.CASCADE, verbose_name='Вид ТО')
    maintenance_date = models.DateField(default=datetime.now, verbose_name='Дата проведения ТО')
    operating_time = models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')
    work_order_number = models.CharField(max_length=32, verbose_name='Заказ-наряд')
    work_order_date = models.DateField(default=datetime.now, verbose_name='дата заказ-наряда')
    service_company = models.ForeignKey('ServiceCompany', on_delete=models.CASCADE, verbose_name='Организация, проводившая ТО', null=True, blank=True)
    autocar = models.ForeignKey(AutoCar, on_delete=models.CASCADE, verbose_name='Заводской номер погрузчика')

    def __str__(self):
        return f'{self.maintenance_date} {self.autocar}'

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'


class Claim(models.Model):
    failure_date = models.DateField(default=datetime.now, verbose_name='Дата отказа')
    operating_time = models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')
    failure_node = models.ForeignKey('FailureNode', on_delete=models.CASCADE, verbose_name='Узел отказа')
    failure_description = models.TextField(blank=True, null=True,  verbose_name='Описание отказа')
    recovery_method = models.ForeignKey('RecoveryMethod', on_delete=models.CASCADE, verbose_name='Способ восстановления')
    spare_parts = models.TextField(blank=True, null=True, verbose_name='Используемые запасные части')
    recovery_date = models.DateField(default=datetime.now, verbose_name='Дата восстановления')
    autocar = models.ForeignKey(AutoCar, on_delete=models.CASCADE, verbose_name='Заводской номер погрузчика') 
    service_company = models.ForeignKey('ServiceCompany', on_delete=models.CASCADE, verbose_name='Сервисная компания', null=True, blank=True)       

    def __str__(self):
        return f'{self.failure_date} {self.autocar}'

    def downtime(self):
        deltatime = self.recovery_date - self.failure_date
        return deltatime.days

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'

# Словари

class MaintenanceType(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Вид технического обслуживания'
        verbose_name_plural = 'Виды технического обслуживания'  


class FailureNode(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узлы отказа' 


class RecoveryMethod(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'


class ServiceCompany(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'   
