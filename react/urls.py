from django.urls import path

from react.apps import ReactConfig
from react.views import index

app_name = ReactConfig.name

urlpatterns = [
    path('vacancy_list/', index, name='vacancy_list'),
]