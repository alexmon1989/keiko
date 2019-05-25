from django.views.generic import TemplateView
from .models import RobotsTxt


class RobotsTxtView(TemplateView):
    template_name = "settings/robots.txt"
    content_type = 'text/plain'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['robots_txt'], created = RobotsTxt.objects.get_or_create()

        return context
