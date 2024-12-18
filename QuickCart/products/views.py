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
        # Split query into words for flexible searching
        search_keywords = re.split(r'[-\s]+', query)  # Split by spaces and hyphens
        filters = Q()

        for word in search_keywords:
            # Perform case-insensitive partial match (icontains)
            filters |= Q(name__icontains=word) | Q(description__icontains=word)

        # Search for exact query match as well
        filters |= Q(name__icontains=query) | Q(description__icontains=query)

        # Filter available products
        results = Product.objects.filter(filters, available=True).distinct()

    return render(request, 'products/product/product_search.html', {
        'query': query,
        'results': results
    })
