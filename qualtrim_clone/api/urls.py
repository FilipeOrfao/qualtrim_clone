from django.urls import path
from api import views

app_name='api'





urlpatterns=[
    path('health',views.health_check,name='health'),
]