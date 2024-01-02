from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import MarkdownContent
import json
 


def custom_404(request, exception):
    return render(request, '/404.html', status=404)
    

# Create your views here.
def index(request):
    template = loader.get_template('products/index.html')
    json_file_path = 'main/data.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    context = {'products_data': data}
    return HttpResponse(template.render(context))

def product(request, product_id):
    template = loader.get_template('products/product.html')
    json_file_path = 'main/data.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Find the product with the specified product_id (converted to string)
    product_data = next((product for product in data if product['id'] == int(product_id)), None)

    # Check if the product_id exists in the data
    if product_data:
        context = {'product_data': product_data}
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseNotFound(render(request, '404.html', status=404))


def account(request):
    return render(request, 'account/index.html')

def basket(request):
    return render(request, 'basket/index.html')

def category(request):
    return render(request, 'category/index.html')

def checkout(request):
    return render(request, 'checkout/index.html')

def contact(request):
    return render(request, 'contact/index.html')

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'info/about.html')

def privacyPolicy(request):
    return render(request, 'info/privacy-policy.html')

def returnsPolicy(request):
    return render(request, 'info/returns-policy.html')

def termsAndConditions(request):
    return render(request, 'info/terms-and-conditions.html')

def login(request):
    return render(request, 'auth/login.html')

def signUp(request):
    return render(request, 'auth/sign-up.html')

def forgotPassword(request):
    return render(request, 'auth/forgot-password.html')

def resetPassword(request):
    return render(request, 'auth/reset-password.html')

def orders(request):
    return render(request, 'orders/index.html')

def products(request):
    return render(request, 'products/index.html')

def search(request):
    return render(request, 'search/index.html')

def settings(request):
    return render(request, 'settings/index.html')

def wishlist(request):
    return render(request, 'wishlist/index.html')

def markdown_content_view(request, slug):
    markdown_content = get_object_or_404(MarkdownContent, slug=slug)
    context = {"markdown_content": markdown_content}
    return render(
        request,
        "markdown_content/index.html",
        context=context
    )