from django.urls import path
from . import views

urlpatterns = [
    path("",views.OrderForm, name="OrderForm"),
    
]
