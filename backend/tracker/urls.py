from django.urls import path
from .views import ProgressView

urlpatterns = [
    path('api/progress', ProgressView.as_view()),  # For POST and GET
]
