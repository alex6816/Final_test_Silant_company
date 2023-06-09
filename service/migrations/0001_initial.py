# Generated by Django 4.2.1 on 2023-05-08 11:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forklifts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailureNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Характер отказа',
                'verbose_name_plural': 'Характеры отказа',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид технического обслуживания',
                'verbose_name_plural': 'Виды технических обслуживаний',
            },
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Способ восстановления',
                'verbose_name_plural': 'Способы восстановления',
            },
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сервисная компания',
                'verbose_name_plural': 'Сервисные компании',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField(default=datetime.datetime.now, verbose_name='Дата проведения ТО')),
                ('operating_time', models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')),
                ('work_order_number', models.CharField(max_length=32, verbose_name='Заказ-наряд')),
                ('work_order_date', models.DateField(default=datetime.datetime.now, verbose_name='дата заказ-наряда')),
                ('autocar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forklifts.autocar', verbose_name='Модель техники')),
                ('maintenance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.maintenancetype', verbose_name='Вид ТО')),
                ('service_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.servicecompany', verbose_name='Организация, проводившая ТО')),
            ],
            options={
                'verbose_name': 'Техническое обслуживание',
                'verbose_name_plural': 'Технические обслуживания',
            },
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failure_date', models.DateField(default=datetime.datetime.now, verbose_name='Дата отказа')),
                ('operating_time', models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')),
                ('failure_description', models.TextField(blank=True, null=True, verbose_name='Описание отказа')),
                ('spare_parts', models.TextField(blank=True, null=True, verbose_name='Используемые запасные части')),
                ('recovery_date', models.DateField(default=datetime.datetime.now, verbose_name='Дата восстановления')),
                ('autocar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forklifts.autocar', verbose_name='Модель техники')),
                ('failure_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.failurenode', verbose_name='Узел отказа')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.recoverymethod', verbose_name='Способ восстановления')),
                ('service_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.servicecompany', verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламации',
            },
        ),
    ]
