from django.urls import path
from products.views import ProductsViews, detail_product_view, CategoriesViews, ProductsCreateView

urlpatterns = [
    path('products/', ProductsViews.as_view()),
    path('products/<int:id>/', detail_product_view),
    path('categories/', CategoriesViews.as_view()),
    path('products/create/', ProductsCreateView.as_view())
]
