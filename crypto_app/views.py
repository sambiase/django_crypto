from django.shortcuts import render
import requests


def crypto_view(request):
    cryptos = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    top_ten = []
    for i in range(0,11):
        top_ten.append(cryptos[i])
    context = {
        "top_ten": top_ten
    }
    return render(request,'index.html', context)
