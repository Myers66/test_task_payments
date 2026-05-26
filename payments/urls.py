from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/data/', views.api_data, name='api_data'),
]