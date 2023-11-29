from django.urls import path

from eshop.views import index, contacts

urlpatterns = [
    path('', contacts),
    path('', index)
]