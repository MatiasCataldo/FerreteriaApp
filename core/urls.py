from django.urls import path
from core.views import AboutView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]