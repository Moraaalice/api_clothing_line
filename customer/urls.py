from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customer import views

urlpatterns = [
    path('customer/', views.customer_detail)
]