from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.shop.models import Order, OrderStatus

import requests


class Command(BaseCommand):
    help = 'Присваивает заказам статусы из Frontpad'

    def handle(self, *args, **options):
        # Список незакрытых заказов
        orders = Order.ready_orders.filter(status__lt=5).exclude(frontpad_id__isnull=True)

        for o in orders:
            params = {
                'secret': settings.FRONTPAD_API_SECRET,
                'order_id': o.frontpad_id
            }

            r = requests.post(f"{settings.FRONTPAD_API_ADDR}?get_status", data=params)

            try:
                data = r.json()
            except ValueError as e:
                self.stdout.write(self.style.ERROR(f"Ошибка в полученных данных: {e}"))
            else:
                if data['result'] == 'success':
                    o.status = OrderStatus.objects.filter(title=data['status']).first()
                    o.save()
                else:
                    if data.get('error') == 'invalid_order_id':
                        o.status, created = OrderStatus.objects.get_or_create(title='Отменён')
                        o.save()
                    self.stdout.write(self.style.ERROR(f"Ошибка в полученных данных: {data.get('error')}"))

        self.stdout.write(self.style.SUCCESS('Завершено'))
