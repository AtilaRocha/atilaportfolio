
from myapp import views
from django.urls import path

urlpatterns = [
    path('', views.open, name='index')
]
