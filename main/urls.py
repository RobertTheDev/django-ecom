from django.urls import path

from . import views

handler404 = 'products.views.custom_404'



urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/", views.product, name="product"),
]

from django.urls import path

from . import views

handler404 = 'main.views.custom_404'



urlpatterns = [
    path("", views.home, name="home"),
    path("account", views.account, name="account"),
    path("basket", views.basket, name="basket"),
    path("category", views.category, name="category"),
    path("checkout", views.checkout, name="checkout"),
    path("contact", views.contact, name="contact"),
    path("info/about", views.about, name="about"),
    path("info/privacy-policy", views.privacyPolicy, name="privacy-policy"),
    path("info/returns-policy", views.returnsPolicy, name="returns-policy"),
    path("info/terms-and-conditions", views.termsAndConditions, name="terms-and-conditions"),
    path("login", views.login, name="login"),
    path("forgot-password", views.forgotPassword, name="forgot-password"),
    path("reset-password", views.resetPassword, name="reset-password"),
    path("sign-up", views.signUp, name="sign-up"),
    path("orders", views.orders, name="orders"),
    path("products/", views.products, name="products"),
    path("products/<int:product_id>/", views.product, name="product"),
    path("search", views.search, name="search"),
    path("settings", views.settings, name="settings"),
    path("wishlist", views.wishlist, name="wishlist"),
]

 