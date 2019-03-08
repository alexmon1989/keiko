from .models import Order


def new_orders_count():
    """Возвращает количество новых заказаов."""
    return Order.objects.filter(status=1).count() or None


def orders_count():
    """Возвращает количество заказаов."""
    return Order.objects.count()
