from django.urls import path
from . import views

app_name = "pua_auth"

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('img_captcha/',views.img_captcha,name='img_captcha'),
    path('register/',views.register,name='register'),
]

