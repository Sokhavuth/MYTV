from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index),
    path('polls/', include('polls.urls')),
    path('admin/', include('admin.urls')),
]