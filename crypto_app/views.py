from django.shortcuts import render
import requests


def crypto_view(request):
    cryptos = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    data = []
    for i in range(0,10):
        data.append(cryptos[i])
    context = {
        "data": data
    }
    return render(request,'index.html', context)
