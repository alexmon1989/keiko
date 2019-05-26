from django.views.generic import TemplateView
from apps.settings.models import SocialUrl
from .models import ContactsModel


class ContactsView(TemplateView):
    template_name = 'contacts/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'], created = ContactsModel.objects.get_or_create()
        context['social_links'] = SocialUrl.objects.filter(is_enabled=True).order_by('-weight')
        return context
