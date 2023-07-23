from django.urls import path
from .views import *

urlpatterns = [
    path("get-person/<int:pk>/", get_person),
    path("get-friend/<int:pk>/", get_friend),
    path("get-gender/<int:pk>/", get_gender),
    path("get-gender-type/<int:pk>", get_gender_type),
]
