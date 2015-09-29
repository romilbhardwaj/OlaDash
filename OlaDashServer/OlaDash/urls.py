from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^requestcab/$', views.requestcab, name='requestcab'),
]