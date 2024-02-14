from django.views.generic import ListView, DetailView

from rh_kosmos.models import Company, RH, Vacancy


class CompanyListView(ListView):
    model = Company
    template_name = 'rh_kosmos/company_list.html'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'rh_kosmos/company_detail.html'


class RHListView(ListView):
    model = RH
    template_name = 'rh_kosmos/rh_list.html'


class RHDetailView(DetailView):
    model = RH
    template_name = 'rh_kosmos/rh_detail.html'


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'rh_kosmos/vacancy_list.html'
    context_object_name = 'vacancies'
