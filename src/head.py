from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
from itertools import islice

print ("Plese, write your N top:")

num = int(input()) #user input amount of coins from list

coins = cg.get_coins_markets(vs_currency="usd") # this is a list

sorted_coins = sorted(coins, key=lambda coin: coin['current_price']) # sorted can accept custom comparator. sort py price

res = list(islice(reversed(sorted_coins), 0, num)) #reverse list for output

for i in res:
    print (i["id"], i["current_price"]) 
