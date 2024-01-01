from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

# Create your views here.
def index(request):
    template = loader.get_template('products/index.html')
    json_file_path = 'products/data.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    context = {'products_data': data}
    return HttpResponse(template.render(context))

def product(request, product_id):
    template = loader.get_template('products/product.html')
    json_file_path = 'products/data.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Find the product with the specified product_id (converted to string)
    product_data = next((product for product in data if product['id'] == str(product_id)), None)

    # Check if the product_id exists in the data
    if product_data:
        context = {'product_data': product_data}
    else:
        context = {'product_data': None}

    return HttpResponse(template.render(context, request))
