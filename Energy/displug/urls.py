from django.urls import path



from . import views

urlpatterns = [
    path('', views.DevicesListView.as_view(), name='index'),
    path('schedule/<slug:slug>', views.DevicesView.as_view(), name='article-detail'),
]