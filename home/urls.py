from django.urls import path
from home import views

urlpatterns = [
    path('endpoints/', views.endpoint, name='endpoint'),
    path('custname/', views.custname, name='custname'),
    path('custdetails/<str:name>', views.customer_detail, name='customer_detail')
]