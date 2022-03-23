from django.urls import path

from shopping.views import ProductListView

app_name = "shopping"


urlpatterns = [
    path('', ProductListView.as_view(), name="index")
]
