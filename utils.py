import logging

def setup_logger():
    logging.basicConfig(
        filename='trading_bot.log',
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO
    )

def validate_order_input(order_type, side, quantity, price=None, stop_price=None):
    if order_type not in ['MARKET', 'LIMIT', 'STOP_MARKET']:
        raise ValueError("Invalid order type")
    if side not in ['BUY', 'SELL']:
        raise ValueError("Invalid side")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if order_type == 'LIMIT' and (price is None or price <= 0):
        raise ValueError("Price required for LIMIT orders")
    if order_type == 'STOP_MARKET' and (stop_price is None or stop_price <= 0):
        raise ValueError("Stop price required for STOP_MARKET orders")
