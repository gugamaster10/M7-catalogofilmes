from django.contrib import admin
from django.urls import path, include

app_main = "main"

urlpatterns = [
    path('', views, homepage, name="homepage"),
]
