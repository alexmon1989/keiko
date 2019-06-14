from .models import Order
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
from hashlib import sha512
from xml.dom.minidom import parseString
import urllib.request


def new_orders_count():
    """Возвращает количество новых заказаов, пригодных к обработке."""
    return Order.ready_orders.filter(status=1).count() or None


def orders_count():
    """Возвращает количество заказаов."""
    return Order.objects.count()


def send_order_email_to_client(order):
    """Высылает клиенту данные заказа на почту."""
    # TODO: сделать красивый шаблон со всеми товарами из корзины
    if order.user_email:
        html_message = loader.render_to_string('shop/email/order.html', {'order': order})
        emails = [order.user_email]
        send_mail(
            subject=f"Заказ №{order.pk}",
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=emails,
            fail_silently=False,
            html_message=html_message)


def create_robokassa_url(order):
    """Формирует ссылку на оплату через Robokassa"""
    mrh_login = settings.ROBOKASSA_MERCHANT_LOGIN
    mrh_pass1 = settings.ROBOKASSA_TEST_PASSWORD1 if settings.ROBOKASSA_IS_TEST else settings.ROBOKASSA_PASSWORD1
    inv_id = order.pk
    inv_desc = f"Оплата заказа №{order.pk} в KEIKO"
    out_summ = order.get_price_total()
    is_test = int(settings.ROBOKASSA_IS_TEST)

    crc = sha512(f"{mrh_login}:{out_summ}:{inv_id}:{mrh_pass1}".encode('utf-8')).hexdigest()

    url = f"https://auth.robokassa.ru/Merchant/Index.aspx?MrchLogin={mrh_login}" \
          f"&OutSum={out_summ}&InvId={inv_id}&Desc={inv_desc}&SignatureValue={crc}&IsTest={is_test}"

    return url


def get_robokassa_sum(out_sum):
    """Получает сумму из Робокассы для платежей без комиссий."""
    url = f"https://auth.robokassa.ru/Merchant/WebService/Service.asmx/CalcOutSumm?MerchantLogin={settings.ROBOKASSA_MERCHANT_LOGIN}" \
          f"&IncCurrLabel=BankCard" \
          f"&IncSum={out_sum}"

    with urllib.request.urlopen(url) as response:
        node = parseString(response.read())
        res = node.getElementsByTagName('OutSum')[0].firstChild.nodeValue

    return res
