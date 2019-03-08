from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.shop.models import Order

import requests


class Command(BaseCommand):
    help = 'Отправляет новые заказы в систему Frontpad'

    def handle(self, *args, **options):
        # Список заказов без frontpad_id
        orders = Order.objects.filter(frontpad_id__isnull=True)

        for o in orders:
            params = {
                'secret': settings.FRONTPAD_API_SECRET,
                # product – массив артикулов товаров
                'product': [p.product.frontpad_id for p in o.cartproduct_set.all()],
                # product_kol – массив количества товаров
                'product_kol': [p.count for p in o.cartproduct_set.all()],
                # product_price – массив цен товаров (установка цены при заказе через API возможна только для товаров
                # с включенной опцией "Изменение цены при создании заказа";
                'product_price': [p.price for p in o.cartproduct_set.all()],
                'street': o.user_address,
                'mail': o.user_email,
                'descr': o.user_comment,
                'name': o.user_name,
                'phone': o.user_phone,
            }

            r = requests.post(f"{settings.FRONTPAD_API_ADDR}?new_order", data=params)

            try:
                data = r.json()
            except ValueError as e:
                self.stdout.write(self.style.Error(f"Ошибка в полученных данных: {e}"))
            else:
                if data['result'] == 'success':
                    o.frontpad_id = int(data['order_id'])
                    o.save()
                else:
                    self.stdout.write(self.style.Error(f"Ошибка в полученных данных: {data.get('error')}"))

        self.stdout.write(self.style.SUCCESS('Успешно завершено'))
