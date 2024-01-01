from django.urls import path

from . import views

handler404 = 'main.views.custom_404'



urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/", views.product, name="product"),
]