from django.urls import path
from .views import crypto_view

urlpatterns = [
    path('',crypto_view,name='crypto_view')
]
