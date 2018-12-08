from django.urls import path
2

from . import views

urlpatterns = [
    path('', views.DevicesListView.as_view(), name='index'),
]