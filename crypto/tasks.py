import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.forms.models import model_to_dict

from .models import Coin

channel_layer = get_channel_layer()


@shared_task
def get_coin_stats():
    coins = []
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    for coin in data:
        state = ''
        obj, created = Coin.objects.get_or_create(name=coin['name'])
        obj.name = coin['name']
        obj.market_cap_rank = coin['market_cap_rank']
        obj.image = coin['image']

        if obj.current_price > coin['current_price']:
            state = 'raise'
        elif obj.current_price == coin['current_price']:
            state = 'same'
        elif obj.current_price < coin['current_price']:
            state = 'fall'

        obj.current_price = coin['current_price']

        obj.high_24h = coin['high_24h']
        obj.low_24h = coin['low_24h']
        obj.price_change_24h = coin['price_change_24h']
        obj.price_change_percentage_24h = coin['price_change_percentage_24h']
        obj.market_cap_change_24h = coin['market_cap_change_24h']
        obj.market_cap_change_percentage_24h = coin['market_cap_change_percentage_24h']

        obj.save()
        # print(obj.current_price)
        new_data = model_to_dict(obj)
        new_data.update({'state': state})
        # print(new_data)
        coins.append(new_data)
    async_to_sync(channel_layer.group_send)('coins', {'type': 'send_coin_data', 'text': coins})
