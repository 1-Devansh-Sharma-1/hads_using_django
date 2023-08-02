# hads_project/urls.py

from django.contrib import admin
from django.urls import path
from hads_app import views

urlpatterns = [
    path('', views.title_page, name='title_page'),
    path('hads_test/', views.hads_test, name='hads_test'),  # URL for the HADS test
    path('result/<int:test_result_id>/', views.hads_result, name='result'),  # URL for the result page
]
