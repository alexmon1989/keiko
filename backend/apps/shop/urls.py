from django.urls import path
from .views import CategoryDetailView, IngredientDetailView, ProductDetailView, CartView, create_order, OrderDetailView

app_name = 'shop'

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('ingredient/<slug:slug>/', IngredientDetailView.as_view(), name='ingredient-detail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('create-order', create_order, name='create-order'),
    path('order-detail/<slug:unique_id>/', OrderDetailView.as_view(), name='order-detail'),
]
