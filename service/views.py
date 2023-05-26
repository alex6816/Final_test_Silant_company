from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from forklifts.models import *
from service.models import *
from service.forms import *
from service.serializers import MaintenanceSerializer, ClaimSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics


class MaintenanceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'service.view_maintenance'
    model = Maintenance
    template_name = 'service/maintenance_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = User.objects.get(pk=self.request.user.pk)
            try:
                profile = UserAcc.objects.get(user=user)
                if profile.is_service:
                    return Maintenance.objects.filter(service_company=profile.service_company)
            except:
                return Maintenance.objects.filter(autocar__client=user)
        else:
            return Maintenance.objects.all()
        

class MaintenanceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_maintenance'
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'service/maintenance_create.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_maintenance'
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'service/maintenance_update.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_maintenance'
    model = Maintenance
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('maintenance_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'maintenance'
        return context
    

class MaintenanceCarListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'service.view_maintenance'
    model = Maintenance
    template_name = 'service/maintenance_car.html'

    def get_queryset(self):
        car = AutoCar.objects.get(pk=self.kwargs["pk"])
        return Maintenance.objects.filter(autocar=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = AutoCar.objects.get(pk=self.kwargs["pk"])
        return context     


class ClaimListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'service.view_claim'
    model = Claim
    template_name = 'service/claim_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = User.objects.get(pk=self.request.user.pk)
            try:
                profile = UserAcc.objects.get(user=user)
                if profile.is_service:
                    return Claim.objects.filter(service_company=profile.service_company)
            except:
                return Claim.objects.filter(autocar__client=user)
        else:
            return Claim.objects.all()  


class ClaimCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_claim'
    model = Claim
    form_class = ClaimForm
    template_name = 'service/claim_create.html'
    success_url = reverse_lazy('claim_list') 


class ClaimUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_claim'
    model = Claim
    form_class = ClaimForm
    template_name = 'service/claim_update.html'
    success_url = reverse_lazy('claim_list')   


class ClaimDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_claim'
    model = Claim
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('claim_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'claim'
        return context 


class ClaimCarListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'service.view_claim'
    model = Claim
    template_name = 'service/claim_car.html'

    def get_queryset(self):
        car = AutoCar.objects.get(pk=self.kwargs["pk"])
        return Claim.objects.filter(autocar=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = AutoCar.objects.get(pk=self.kwargs["pk"])
        return context  


class MaintenanceDescriptionView(TemplateView):
    template_name = 'service/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maintenance = Maintenance.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'maintenance_type':
            context['atribute'] = maintenance.maintenance_type
            context['description'] = maintenance.maintenance_type.description
        elif atribute == 'service_company':
            context['atribute'] = maintenance.service_company
            context['description'] = maintenance.service_company.description
        return context  


class ClaimDescriptionView(TemplateView):
    template_name = 'service/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        claim = Claim.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'failure_node':
            context['atribute'] = claim.failure_node
            context['description'] = claim.failure_node.description
        elif atribute == 'recovery_method':
            context['atribute'] = claim.recovery_method
            context['description'] = claim.recovery_method.description
        elif atribute == 'service_company':
            context['atribute'] = claim.service_company
            context['description'] = claim.service_company.description
        return context 


# API
class MaintenanceListAPI(generics.ListAPIView):
    serializer_class = MaintenanceSerializer
    queryset = Maintenance.objects.all()


class MaintenanceUserListAPI(generics.ListAPIView):
    serializer_class = MaintenanceSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Maintenance.objects.filter(autocar__client=user)
        elif type(user) == str:
            queryset = Maintenance.objects.filter(autocar__client__username=user)
        return queryset 


class MaintenanceDetailAPI(generics.RetrieveAPIView):
    serializer_class = MaintenanceSerializer

    def get_object(self):
        obj = Maintenance.objects.get(pk=self.kwargs['pk'])
        return obj


class ClaimListAPI(generics.ListAPIView):
    serializer_class = ClaimSerializer
    queryset = Claim.objects.all() 


class ClaimUserListAPI(generics.ListAPIView):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Claim.objects.filter(autocar__client=user)
        elif type(user) == str:
            queryset = Claim.objects.filter(autocar__client__username=user)
        return queryset


class ClaimDetailAPI(generics.RetrieveAPIView):
    serializer_class = ClaimSerializer

    def get_object(self):
        obj = Claim.objects.get(pk=self.kwargs['pk'])
        return obj                              





