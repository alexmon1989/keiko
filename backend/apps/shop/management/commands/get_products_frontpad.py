from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.shop.models import Product

import requests


class Command(BaseCommand):
    help = 'Выгружает из Frontpad информацию о продуктах и записывает в БД.'

    def prepare_title(self, title):
        return title.replace('  ', ' ')

    def handle(self, *args, **options):
        params = {'secret': settings.FRONTPAD_API_SECRET}

        r = requests.post(f"{settings.FRONTPAD_API_ADDR}?get_products", data=params)

        try:
            data = r.json()
        except ValueError as e:
            self.stdout.write(self.style.Error(f"Ошибка в полученных данных: {e}"))
        else:
            if data['result'] == 'success':
                data_len = len(data['product_id'])
                for i in range(data_len):
                    if not Product.objects.filter(frontpad_id=data['product_id'][i]).exists():
                        product = Product.objects.create(
                            title=self.prepare_title(data['name'][i]),
                            frontpad_id=data['product_id'][i],
                            price=data['price'][i],
                        )
                        self.stdout.write(f"Создан продукт \"{product.title}\" "
                                          f"(цена - {product.price}, "
                                          f"frontpad_id - {product.frontpad_id})")
            else:
                self.stdout.write(self.style.Error(f"Ошибка в полученных данных: {data.get('error')}"))

        self.stdout.write(self.style.SUCCESS('Успешно завершено'))
