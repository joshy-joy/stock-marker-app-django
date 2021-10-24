import os

from celery import Celery
from .models import SellOrder, BuyOrder, CompletedOrder

from portfolio.models import Portfolio

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
# app.autodiscover_tasks()

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(1.0, stock_exchange.s(), name='stock_exchange')


@app.task(bind=True)
def stock_exchange(self):
    try:
        buy = BuyOrder.objects.all().order_by('-price')
        for each_buy in buy.iterator():
            sell = SellOrder.objects.all().order_by('price')
            for each_sell in sell.iterator():
                if each_buy.symbol == each_sell.symbol and each_buy.user_id != each_sell.user_id:
                    if each_buy.quantity >= each_sell.quantity and each_buy.price >= each_sell.price:
                        order = SellOrder.objects.get(id=each_sell.id)
                        update_completed_order(order.user_id, order.symbol, order.quantity, order.price, 'sell')
                        update_portfolio(each_buy, each_sell, order.quantity)
                        update_buy_order(each_buy)
                        order.delete()
                    elif each_buy.quantity  < each_sell.quantity and each_buy.price >= each_sell.price:
                        order = BuyOrder.objects.get(id=each_buy.id)
                        update_completed_order(order.user_id, order.symbol, order.quantity, order.price, 'buy')
                        update_portfolio(each_buy, each_sell, order.quantity)
                        update_sell_order(each_sell)
                        order.delete()
        print("stock exchange matching engine stops -------------->")
    except Exception as e:
        print(str(e))


def update_completed_order(user_id, symbol, quantity, price, order_type):
    try:
        order = CompletedOrder(user_id=user_id, symbol=symbol, quantity=quantity, price=price, type=order_type)
        order.save()
    except Exception as e:
        print(str(e))

def update_buy_order(each_buy):
    try:
        order = BuyOrder.objects.get(id=each_buy.id)
        order.quantity -= each_buy.quantity
        order.save()
    except BuyOrder.DoesNotExist:
        print("No buy data found for curresponding id")

def update_sell_order(each_sell):
    try:
        order = SellOrder.objects.get(id=each_sell.id)
        order.quantity -= each_sell.quantity
        order.save()
    except SellOrder.DoesNotExist:
        print("No sell data found for curresponding id")


def update_portfolio(each_buy, each_sell, quantity):
    #updating buy order in portfolio
    try:
        portfolio = Portfolio.objects.filter(user_id=each_buy.user_id, symbol=each_buy.symbol).get()
        print("portfolio update----->", portfolio)
        portfolio.quantity += quantity
        portfolio.save()
    except Portfolio.DoesNotExist:
        portfolio = Portfolio(user_id = each_buy.user_id, symbol=each_buy.symbol, quantity=quantity, price=each_buy.price)
        print("portfolio save----->", portfolio)
        portfolio.save()

    try:
        #updating sell order in portfolio
        order = Portfolio.objects.filter(user_id=each_sell.user_id, symbol=each_sell.symbol).get()
        print("portfolio delete ----->", order)
        if (order.quantity - quantity) == 0:
            order.delete()
        else:
            order.quantity -= quantity
            order.save()
    except Portfolio.DoesNotExist:
        print("Stock not in portfolio")