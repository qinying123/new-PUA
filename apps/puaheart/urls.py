from django.urls import path
from .import views

app_name = 'puaheart'

urlpatterns = [
    path('', views.choose, name='choose'),
    path('one/', views.one, name='one'),
    path('two/', views.two, name='two')
]