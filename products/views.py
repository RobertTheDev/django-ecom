from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('products/index.html')
    return HttpResponse(template.render())

def product(request, product_id):
    template = loader.get_template('products/product.html')
    context = {'product_id': product_id}
    return HttpResponse(template.render(context, request))