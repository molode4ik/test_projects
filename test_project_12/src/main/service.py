from src.main.models import StockPrice


def save_response(data):
    for response_key, response_value in data.items():
        stock_item = StockPrice(timestamp=response_key,
                                open_price=float(response_value.get('1. open')),
                                high_price=float(response_value.get('2. high')),
                                low_price=float(response_value.get('3. low')),
                                close_price=float(response_value.get('4. close')),
                                volume=int(response_value.get('5. volume')))
        stock_item.save()

