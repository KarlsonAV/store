from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView, FilterByCategory


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<uuid:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<uuid:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('filtered_by_category/', FilterByCategory.as_view(), name='filtered_by_category'),
]