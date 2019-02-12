from django.urls import path
from .views import CategoryDetailView, IngredientDetailView

app_name = 'shop'

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('ingredient/<slug:slug>/', IngredientDetailView.as_view(), name='ingredient-detail'),
]
