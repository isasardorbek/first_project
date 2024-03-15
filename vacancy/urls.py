from django.urls import path, include

from .views import employer_view, employer_detail, new_job, my_job, clicks


urlpatterns = [
    path('', employer_view),
    path('<int:id>/', employer_detail),
    path('new-job/<int:id>/', new_job),
    path('my-jobs/<int:id>/', my_job),
    path('clicks/<int:id>/', clicks),
]
