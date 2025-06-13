# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.code_view, name='code_view'),

]
