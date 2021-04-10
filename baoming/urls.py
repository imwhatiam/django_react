from django.urls import path

from baoming.views import Persons

urlpatterns = [
    path('persons/', Persons.as_view(), name='api-persons'),
]
