from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    ROLES = (
        ('APPLICANT', 'Applicant'),
        ('RH', 'RH'),
        ('COMPANY', 'Company'),
    )

    username = None
    role = models.CharField(max_length=15, choices=ROLES, verbose_name='Roles')
    email = models.EmailField(unique=True, verbose_name='Email')

    phone_number = models.CharField(max_length=40, verbose_name='Phone number', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.role}'


@receiver(pre_save, sender=User)
def hash_user_password(sender, instance, **kwargs):
    if instance._state.adding:
        instance.set_password(instance.password)
