from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from forklifts.models import *
from service.models import *
from forklifts.forms import *
from forklifts.serializers import AutoCarSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics


# Главная
class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('car_list')
        else:
            return redirect('car_search_list')
        

class CarSearchView(ListView):
    model = AutoCar
    template_name = 'forklifts/car_search.html'
    queryset = AutoCar.objects.all()


class CarListView(LoginRequiredMixin, ListView):
    model = AutoCar
    template_name = 'forklifts/car_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = User.objects.get(pk=self.request.user.pk)
            try:
                profile = UserAcc.objects.get(user=user)
                if profile.is_service:
                    return AutoCar.objects.filter(service_company=profile.service_company)
            except:
                return AutoCar.objects.filter(client=user)
        else:
            return AutoCar.objects.all()    
        

class CarDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'forklifts.view_car'
    model = AutoCar
    template_name = 'forklifts/car_view.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  


class CarCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'forklifts.add_autocar'
    model = AutoCar
    form_class = AutoCarForm
    template_name = 'forklifts/car_create.html'
    success_url = reverse_lazy('car_list') 


class CarUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'forklifts.change_autocar'
    model = AutoCar
    form_class = AutoCarForm
    template_name = 'forklifts/car_update.html'
    success_url = reverse_lazy('car_list')  


class CarDescriptionView(TemplateView):
    template_name = 'service/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = AutoCar.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'car_model':
            context['atribute'] = car.car_model
            context['description'] = car.car_model.description
        elif atribute == 'engine_model':
            context['atribute'] = car.engine_model
            context['description'] = car.engine_model.description
        elif atribute == 'transmission_model':
            context['atribute'] = car.transmission_model
            context['description'] = car.transmission_model.description
        elif atribute == 'drive_axle_model':
            context['atribute'] = car.drive_axle_model
            context['description'] = car.drive_axle_model.description
        elif atribute == 'steerable_axle_model':
            context['atribute'] = car.steerable_axle_model
            context['description'] = car.steerable_axle_model.description
        elif atribute == 'equipment':
            context['atribute'] = 'Комплектация'
            context['description'] = car.equipment
        elif atribute == 'service_company':
            context['atribute'] = car.service_company
            context['description'] = car.service_company.description
        return context  


class CarDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'forklifts.delete_car'
    model = AutoCar
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('car_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'car'
        return context 


# API
class CarListAPI(generics.ListAPIView):
    serializer_class = AutoCarSerializer
    queryset = AutoCar.objects.all()


class CarUserListAPI(generics.ListAPIView):
    serializer_class = AutoCarSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = AutoCar.objects.filter(client=user)
        elif type(user) == str:
            queryset = AutoCar.objects.filter(client__username=user)
        return queryset 


class CarDetailAPI(generics.RetrieveAPIView):
    serializer_class = AutoCarSerializer

    def get_object(self):
        obj = AutoCar.objects.get(pk=self.kwargs['pk'])
        return obj                       