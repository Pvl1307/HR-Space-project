from rest_framework import serializers

from rh_kosmos.models import Company, Applicant, RH, Vacancy


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'description', 'num_of_employees', 'logo',)


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('applicant', 'skills', 'status_of_searching',)


class RHSerializer(serializers.ModelSerializer):
    class Meta:
        model = RH
        fields = ('rh', 'services', 'price', 'subscription',)


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('owner', 'title', 'description', 'salary',)
