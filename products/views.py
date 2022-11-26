from django.shortcuts import render, redirect
from products.models import Category, Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from users.utils import get_user_from_request

# Create your views here.


def categories_view(request, **kwargs):
    if request.method == 'GET':
        categories = Category.objects.all()

        data = {
            'categories': categories,
            'user': get_user_from_request(request)
        }

        return render(request, 'categories/categories.html', context=data)


def products_view(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')

        if category_id:
            products = Product.objects.filter(categories__in=[category_id])
        else:
            products = Product.objects.all()

        products = [{
            'id': product.id,
            'image': product.image,
            'title': product.title,
            'price': product.price,
            'colour': product.colour,
            'characteristics': product.characteristics,
            'descriptions': product.description,
            'categories': product.categories.all()
        }for product in products]

        data = {
            'products': products,
            'user': get_user_from_request(request)
        }

        return render(request, 'products/products.html', context=data)


def detail_product_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        reviews = Review.objects.filter(product_id=id)

        data = {
            'product': product,
            'categories': product.categories.all(),
            'reviews': reviews,
            'form': ReviewCreateForm,
            'user': get_user_from_request(request)
        }

        return render(request, 'products/detail.html', context=data)

    if request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                author_id=2,
                text=form.cleaned_data.get('text'),
                rate=form.cleaned_data.get('rate'),
                product_id=id
            )
            return redirect(f'/products/{id}/')
        else:
            product = Product.objects.get(id=id)
            reviews = Review.objects.filter(product_id=id)

            data = {
                'product': product,
                'categories': product.categories.all(),
                'reviews': reviews,
                'form': form,
                'user': get_user_from_request(request)
            }

            return render(request, 'products/detail.html', context=data)


def products_create_view(request):
    if request.method == 'GET':

        data = {
            'form': ProductCreateForm,
            'user': get_user_from_request(request)
        }

        return render(request, 'products/create.html', context=data)

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                author_id=1,
                title=form.cleaned_data.get('title'),
                price=form.cleaned_data.get('price'),
                description=form.cleaned_data.get('description'),
                characteristics=form.cleaned_data.get('characteristics')
            )
            return redirect('/products')
        else:
            data = {
                'form': form,
                'user': get_user_from_request(request)
            }
            return render(request, 'products/create.html', context=data)
