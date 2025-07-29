from binance.client import Client
from binance.enums import *
from config import API_KEY, API_SECRET, BASE_URL, SYMBOL
from utils import setup_logger, validate_order_input
import logging

class BasicBot:
    def __init__(self):
        setup_logger()
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL

    def place_order(self, order_type, side, quantity, price=None, stop_price=None):
        try:
            validate_order_input(order_type, side, quantity, price, stop_price)

            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=SYMBOL,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=SYMBOL,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=SYMBOL,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_STOP_MARKET,
                    stopPrice=stop_price,
                    closePosition=False,
                    quantity=quantity,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            logging.info(f"Order placed: {order}")
            return order

        except Exception as e:
            logging.error(f"Order failed: {str(e)}")
            return {"error": str(e)}
