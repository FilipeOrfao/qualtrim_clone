from django.urls import path
from api import views

app_name = "api"


urlpatterns = [
    path("health/", views.health_check, name="health"),
    path(
        "dollar_cost_average/<str:ticker>/",
        views.dollar_cost_average,
        name="dollar_cost_average",
    ),
]
