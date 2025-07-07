from celery import Celery
from config import BROKER_URL
import json

app = Celery('main', backend='rpc://', broker=BROKER_URL)

@app.task()
def get_buyers_data(data):
    data = json.loads(data)

    result = {
        "couponId": data["couponId"],
        "buyerName": "Lucas Souza",
        "buyerBirthDate": "1994-03-29",
        "buyerDocument": "419.438.578.98"
    }

    return result