"""one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from apps.news import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('news/', include("apps.news.urls")),
    path('cms/',include("apps.cms.urls")),
    path('account/',include("apps.pua_auth.urls")),
    path('',views.index,name='index'),
    path('baike/',include("apps.baike.urls")),
    path('ueditor/',include("apps.ueditor.urls")),
    path('puaheart/', include('apps.puaheart.urls')),
    path('we/', include('apps.we.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)