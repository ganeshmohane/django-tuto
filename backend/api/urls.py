from django.urls import path
from .views import get_all_students, create_student, login, predict_placement

urlpatterns = [
    path('all_students/', get_all_students),
    path('create_student/', create_student),
    path('login/',login),
    path('predict/', predict_placement)
]