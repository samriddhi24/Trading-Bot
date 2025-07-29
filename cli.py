from bot import BasicBot

def main():
    bot = BasicBot()

    print("=== Binance Futures Trading Bot (Testnet) ===")
    order_type = input("Order type (MARKET / LIMIT / STOP_MARKET): ").strip().upper()
    side = input("Side (BUY / SELL): ").strip().upper()
    quantity = float(input("Quantity: "))
    price = None
    stop_price = None

    if order_type == "LIMIT":
        price = float(input("Limit Price: "))
    elif order_type == "STOP_MARKET":
        stop_price = float(input("Stop Price: "))

    result = bot.place_order(order_type, side, quantity, price, stop_price)
    print("Result:", result)

if __name__ == "__main__":
    main()
