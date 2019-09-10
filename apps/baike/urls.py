from django.urls import path
from . import views

app_name = 'baike'

urlpatterns = [
    path('',views.baike_index,name='baike_index'),
]
