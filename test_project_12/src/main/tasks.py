import requests
from celery import shared_task
from proj.celery import app
from src.main.service import save_response


@app.task
def get_api():
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo')
    if response.status_code == 200:
        save_response(response.json().get('Time Series (5min)'))
        return True
    return False
