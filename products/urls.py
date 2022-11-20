from django.urls import path
from products.views import products_view, detail_product_view, categories_view

urlpatterns = [
    path('products/', products_view),
    path('products/<int:id>/', detail_product_view),
    path('categories/', categories_view)
]
