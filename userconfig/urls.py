
from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path('', views.register, name="join"),
    path('login/', views.login, name="login"),
]
