from django.urls import path
from .views import index

app_name = 'delivery'

urlpatterns = [
    path('', index, name='index'),
]
