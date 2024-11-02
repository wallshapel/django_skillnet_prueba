from django.urls import path
from . import views

urlpatterns = [
    path('person/', views.person_form_view, name='person_form'),
]
