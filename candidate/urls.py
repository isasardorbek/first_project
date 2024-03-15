
from django.contrib import admin
from django.urls import path, include

from .views import candidate_view, job_detail

urlpatterns = [
    path('', candidate_view),
    path('<int:id>/', job_detail)
]
