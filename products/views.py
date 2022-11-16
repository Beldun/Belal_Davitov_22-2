from django.shortcuts import render
from products.models import Category, Product, Review

# Create your views here.


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        data = {
            'categories': categories
        }

        return render(request, 'categories/categories.html', context=data)


def products_view(request):
    if request.method == 'GET':
        products = [{
            'id': product.id,
            'image': product.image,
            'title': product.title,
            'price': product.price,
            'colour': product.colour,
            'characteristics': product.characteristics,
            'descriptions': product.description,
            'categories': product.categories.all()
        }for product in Product.objects.all()]

        data = {
            'products': products
        }

        return render(request, 'products/products.html', context=data)


def detail_product_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        reviews = Review.objects.filter(product_id=id)

        data = {
            'product': product,
            'categories': product.categories.all(),
            'reviews': reviews
        }

        return render(request, 'products/detail.html', context=data)
