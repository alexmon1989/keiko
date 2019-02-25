from django.urls import path
from .views import CategoryDetailView, IngredientDetailView, ProductDetailView, CartView, order

app_name = 'shop'

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('ingredient/<slug:slug>/', IngredientDetailView.as_view(), name='ingredient-detail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('order', order, name='order'),
]
