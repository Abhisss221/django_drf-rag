from django.urls import path
# from .views import HealthCheck
from .views import HealthCheck, AskAPIView

urlpatterns = [
    path("health/", HealthCheck.as_view()),
    path("ask/", AskAPIView.as_view()),
]
