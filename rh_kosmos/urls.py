from django.urls import path

from rh_kosmos.apps import RhKosmosConfig
from rh_kosmos.views import CompanyListView, CompanyDetailView, RHListView, RHDetailView, VacancyListView

app_name = RhKosmosConfig.name

urlpatterns = [
    path('company_list/', CompanyListView.as_view(), name='company_list'),
    path('company_detail/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),

    path('rg_list/', RHListView.as_view(), name='rh_list'),
    path('rh_detail/<int:pk>/', RHDetailView.as_view(), name='rh_detail'),

    path('vacancy-list/', VacancyListView.as_view(), name='vacancy_list'),
]
