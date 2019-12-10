from django.contrib import admin
from django.urls import path

from .views import FeedbackView, QRListView
from django.views.generic import TemplateView
app_name = 'qrservice'

urlpatterns = [
    path('feedback/', FeedbackView.as_view()),
    path('ok/', TemplateView.as_view(template_name='qrservice/ok.html'), name='ok'),
    path('qr/all/', QRListView.as_view())
    
] 
