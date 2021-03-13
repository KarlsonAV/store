from django.urls import path

from .views import OrdersPageView, charge


urlpatterns = [
    path('<uuid:pk>', OrdersPageView.as_view(), name='orders'),
    path('<uuid:pk>/charge/', charge, name='charge'),
]