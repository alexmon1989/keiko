from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import PromotionArticle


class PromotionListView(ListView):
    model = PromotionArticle
    paginate_by = 20
    template_name = 'promotions/list/list.html'

    def get_queryset(self):
        return PromotionArticle.objects.filter(is_enabled=True).order_by('-created_at')


class PromotionDetailView(DetailView):
    model = PromotionArticle
    template_name = 'promotions/detail/detail.html'

    def get_queryset(self):
        return PromotionArticle.objects.filter(is_enabled=True)
