from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact_form, name='contact'),
    path('survey/', views.survey_view, name='survey'),
    path('survey/submit/', views.survey_submit, name='survey_submit'),
]
