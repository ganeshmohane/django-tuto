from django.urls import path
from .views import get_all_students, create_student

urlpatterns = [
    path('all_students/', get_all_students),
    path('create_student/', create_student)
]