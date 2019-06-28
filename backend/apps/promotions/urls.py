from django.urls import path
from .views import (PromotionDetailView, PromotionListView)

app_name = 'promotions'

urlpatterns = [
    path('', PromotionListView.as_view(), name='list'),
    path('<slug:slug>/', PromotionDetailView.as_view(), name='detail'),
]
