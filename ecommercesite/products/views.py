from django.shortcuts import get_object_or_404, render, render
from django.db.models import Q
import re

# Create your views here.

from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/product/list.html', {'category': category, 
                                                          'categories': categories,
                                                            'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'products/product/detail.html', {'product': product})


def product_search(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        # Preprocess query: Split words and match boundaries
        search_keywords = re.split(r'\s+', query)  # Split query into words
        filters = Q()

        for word in search_keywords:
            # Match whole words or boundary words using iregex
            regex = r'\b' + re.escape(word) + r'\b'
            filters |= Q(name__iregex=regex) | Q(description__iregex=regex)

        results = Product.objects.filter(filters, available=True).distinct()

    return render(request, 'products/product/product_search.html', {
        'query': query,
        'results': results
    })