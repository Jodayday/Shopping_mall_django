from django.urls import path

from shopping.views import ProductListView, ProductCreateView, ProductDetail, OrderView, ProductOrderView

app_name = "shopping"


urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('<int:pk>/', ProductDetail.as_view(), name="detail"),
    path('<int:pk>/order/', OrderView.as_view(), name="order"),
    path('order/', ProductOrderView.as_view(), name="order_list"),
]
