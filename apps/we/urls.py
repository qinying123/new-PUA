from django.urls import path
from .import views

app_name = 'we'

urlpatterns = [
    path('', views.contract, name='contract'),

]