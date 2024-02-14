from django.contrib import admin

from rh_kosmos.models import Company, Applicant, RH, Vacancy


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'description', 'num_of_employees',)


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'skills', 'status_of_searching',)


@admin.register(RH)
class RHAdmin(admin.ModelAdmin):
    list_display = ('rh', 'services', 'price', 'subscription',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'description', 'salary', )
