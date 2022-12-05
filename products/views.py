from django.shortcuts import render, redirect
from products.models import Category, Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from users.utils import get_user_from_request
from django.views.generic import ListView, CreateView

# Create your views here.

PAGINATION_LIMIT = 3


class CategoriesViews(ListView):
    model = Category
    template_name = 'categories/categories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'categories': self.get_queryset(),
            'user': get_user_from_request(self.request)
        }


class ProductsViews(ListView):
    model = Product
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        return {
            'products': kwargs['products'],
            'user': get_user_from_request(self.request),
            'max_page': range(1, kwargs['max_page']+1)
        }

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            category_id = request.GET.get('category_id')
            search_text = request.GET.get('search')
            page = int(request.GET.get('page', 1))

            if category_id:
                products = Product.objects.filter(categories__in=[category_id])
            else:
                products = Product.objects.all()

            if search_text:
                products = products.filter(title__icontains=search_text)

            products = [{
                'id': product.id,
                'image': product.image,
                'title': product.title,
                'price': product.price,
                'colour': product.colour,
                'characteristics': product.characteristics,
                'descriptions': product.description,
                'categories': product.categories.all()
            } for product in products]

            max_page = round(products.__len__() / PAGINATION_LIMIT)
            products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

            return render(request, 'products/products.html', context=self.get_context_data(
                products=products,
                max_page=max_page
            ))


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
                author_id=request.user.id,
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


class ProductsCreateView(ListView, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/create.html'

    def get_context_data(self, *args, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class,
            'user': get_user_from_request(self.request)
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            self.model.objects.create(
                author_id=request.user.id,
                title=form.cleaned_data.get('title'),
                price=form.cleaned_data.get('price'),
                description=form.cleaned_data.get('description'),
                characteristics=form.cleaned_data.get('characteristics')
            )
            return redirect('/products')
        else:
            return render(request, 'products/create.html', context=self.get_context_data(form=form))
