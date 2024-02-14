from django.db import models

from users.models import User


class Company(models.Model):
    """Модель компании, которую будут искать соискатели"""
    name = models.CharField(max_length=200, verbose_name='Company name')
    description = models.TextField(verbose_name='Company description')
    num_of_employees = models.IntegerField(verbose_name='Number of employees')
    logo = models.ImageField(upload_to='company/', verbose_name='Logo')

    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Company owner')

    def __str__(self):
        return f'Company-{self.name}, owner-{self.owner}'

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Applicant(models.Model):
    """Модель соискателя, который будет искать работу"""
    STATUSES = (
        ('ACTIVE_SEARCH', 'Active search'),
        ('IN_CONSIDERATION', 'In consideration'),
        ('BUSY', 'Busy'),
    )

    applicant = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Applicant personal data')
    skills = models.TextField(verbose_name='Applicant skills')
    status_of_searching = models.CharField(max_length=20, choices=STATUSES, verbose_name='Status of searching')

    def __str__(self):
        return f'{self.applicant}, status-{self.status_of_searching}'

    class Meta:
        verbose_name = 'Applicant'
        verbose_name_plural = 'Applicants'


class RH(models.Model):
    """Модель RH, который будет помогать искать соискателю компанию"""
    rh = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='RH data')
    services = models.TextField(verbose_name='RH services')
    price = models.IntegerField(verbose_name='Price for service')
    subscription = models.BooleanField(verbose_name='Subscription')

    def __str__(self):
        return f'{self.rh}, price-{self.price} rub.'

    class Meta:
        verbose_name = 'RH'
        verbose_name_plural = 'RHs'


class Vacancy(models.Model):
    """Вакансия, которую представляет компания"""
    owner = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Company vacancy')
    title = models.CharField(max_length=200, verbose_name='Title of vacancy')
    description = models.TextField(verbose_name='Description of vacancy')
    salary = models.IntegerField(verbose_name='Salary per month')

    def __str__(self):
        return f'{self.title}, salary-{self.salary} rub. per moth'

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
