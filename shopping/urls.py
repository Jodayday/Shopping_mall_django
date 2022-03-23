from django.urls import path

from shopping.views import ProductListView, ProductCreateView

app_name = "shopping"


urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('create/', ProductCreateView.as_view(), name="create"),
]
