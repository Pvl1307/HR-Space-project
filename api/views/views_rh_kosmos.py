from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsOwnerOrAdmin
from api.serailizers.serializers_rh_kosmos import CompanySerializer, ApplicantSerializer, RHSerializer, \
    VacancySerializer
from rh_kosmos.models import Company, Applicant, RH, Vacancy


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_update(self, serializer):
        serializer.save()

    def perform_create(self, serializer):
        serializer.save()


class ApplicantViewSet(ModelViewSet):
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_update(self, serializer):
        serializer.save()

    def perform_create(self, serializer):
        serializer.save()


class RHViewSet(ModelViewSet):
    serializer_class = RHSerializer
    queryset = RH.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_update(self, serializer):
        serializer.save()

    def perform_create(self, serializer):
        serializer.save()


class VacancyViewSet(ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    def perform_update(self, serializer):
        serializer.save()

    def perform_create(self, serializer):
        serializer.save()
