from django.urls import path
from products.views import ProductsViews, DetailProductView, CategoriesViews, ProductsCreateView

urlpatterns = [
    path('products/', ProductsViews.as_view()),
    path('products/<int:id>/', DetailProductView.as_view()),
    path('categories/', CategoriesViews.as_view()),
    path('products/create/', ProductsCreateView.as_view())
]
