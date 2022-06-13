"""django_ai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from sentiment_analysis.views import sa_view, post_sa_view, get_sa_view, get_sa_input_view, get_sa_output_view

app_name = 'sentiment_analysis'

urlpatterns = [
    path('sa/', sa_view),
    path('ajax/sa_submit', post_sa_view, name ='sa_submit'),
    path('ajax/get_sa_info', get_sa_view, name = 'get_sa_info'),
    path('ajax/get_sa_input_image', get_sa_input_view, name = 'get_sa_input_image'),
    path('ajax/get_sa_output_image', get_sa_output_view, name = 'get_sa_output_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)