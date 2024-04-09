from django.urls import path
from wallflowerApp import views

urlpatterns = [
    path("", views.index, name='index'),
]