from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('valid', views.valid),
    path('redeem', views.redeem),
]