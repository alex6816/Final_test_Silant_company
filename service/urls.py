from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('maintenances/', MaintenanceListView.as_view(), name='maintenance_list'),
    path('claims/', ClaimListView.as_view(), name='claim_list'),
    path('car/<pk>/maintenances', MaintenanceCarListView.as_view(), name='car_maintenance'),
    path('car/<pk>/claims', ClaimCarListView.as_view(), name='car_claim'),
    path('maintenance/create', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('claim/create', ClaimCreateView.as_view(), name='claim_create'),
    path('maintenance/<pk>/update', MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('claim/<pk>/update', ClaimUpdateView.as_view(), name='claim_update'),
    path('maintenance/<pk>/delete', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    path('claim/<pk>/delete', ClaimDeleteView.as_view(), name='claim_delete'),
    path('maintenance/<pk>/description/<atribute>', MaintenanceDescriptionView.as_view(),  name='maintenance_description'),
    path('claim/<pk>/description/<atribute>', ClaimDescriptionView.as_view(), name='claim_description'),
    path('api/maintenances/', MaintenanceListAPI.as_view(), name='maintenance_list_api'),
    path('api/<user>/maintenances/', MaintenanceUserListAPI.as_view(), name='user_maintenance_list_api'),
    path('api/maintenance/<pk>/', MaintenanceDetailAPI.as_view(), name='maintenance_detail_api'),
    path('api/claims/', ClaimListAPI.as_view(), name='claim_list_api'),
    path('api/<user>/claims/', ClaimUserListAPI.as_view(), name='user_claim_list_api'),
    path('api/claim/<pk>/', ClaimDetailAPI.as_view(), name='claim_detail_api'),
]