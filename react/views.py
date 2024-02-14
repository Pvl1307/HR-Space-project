from django.shortcuts import render

from rh_kosmos.models import Vacancy


def index(request):
    vacancies = Vacancy.objects.select_related('owner').all()
    return render(request, 'react/vacancy_list.html', {'vacancies': vacancies})
