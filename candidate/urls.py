
from django.contrib import admin
from django.urls import path, include

from .views import candidate_view, job_detail, complete_profile

urlpatterns = [
    path('', candidate_view),
    path('<int:id>/', job_detail),
    path('profile/', complete_profile)
]
