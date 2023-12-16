from django.urls import path
from .views import index, rate_survey, contact

urlpatterns = [
    path('', index, name='index'),
    path('rate-survey', rate_survey, name='rate_survey'),
    # path('contact', contact, name='contact'),
]