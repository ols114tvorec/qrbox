from django.contrib import admin
from django.urls import path

from .views import FeedbackView

app_name = 'qrservice'

urlpatterns = [
    path('feedback/', FeedbackView.as_view())
]
