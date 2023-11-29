from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.contacts),
    path('contacts/', views.index)
]