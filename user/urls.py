from django.urls import path


app_name = "user"


urlpatterns = [
    path('', index, name="index")
]
