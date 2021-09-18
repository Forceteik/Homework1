The outputting top of coins

Installation:
pip install pycoingecko


Usage:
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
from itertools import islice

Examples:
input- 3
output- [{'id': 'wrapped-bitcoin', 'symbol': 'wbtc', 'name': 'Wrapped Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/7598/large/wrapped_bitcoin_wbtc.png?1548822744', 'current_price': 48340, 'market_cap': 9981617515, 'market_cap_rank': 20, 'fully_diluted_valuation': 9981617515, 'total_volume': 305449058, 'high_24h': 48845, 'low_24h': 47130, 'price_change_24h': 1092.04, 'price_change_percentage_24h': 2.31129, 'market_cap_change_24h': 253283639, 'market_cap_change_percentage_24h': 2.60357, 'circulating_supply': 206320.75943419, 'total_supply': 206320.75943419, 'max_supply': 206320.75943419, 'ath': 64565, 'ath_change_percentage': -25.12997, 'ath_date': '2021-04-14T12:00:05.340Z', 'atl': 3139.17, 'atl_change_percentage': 1439.89629, 'atl_date': '2019-04-02T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-18T19:01:26.913Z'}, 
	{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 48367, 'market_cap': 910446548458, 'market_cap_rank': 1, 'fully_diluted_valuation': 1015930733247, 'total_volume': 28042506718, 'high_24h': 48887, 'low_24h': 47062, 'price_change_24h': 939.97, 'price_change_percentage_24h': 1.98192, 'market_cap_change_24h': 20281449417, 'market_cap_change_percentage_24h': 2.27839, 'circulating_supply': 18819568.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 64805, 'ath_change_percentage': -25.36179, 'ath_date': '2021-04-14T11:54:46.763Z', 'atl': 67.81, 'atl_change_percentage': 71231.36115, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-18T19:01:40.988Z'}, 
	{'id': 'huobi-btc', 'symbol': 'hbtc', 'name': 'Huobi BTC', 'image': 'https://assets.coingecko.com/coins/images/12407/large/Unknown-5.png?1599624896', 'current_price': 48421, 'market_cap': 1934922523, 'market_cap_rank': 72, 'fully_diluted_valuation': 1934922523, 'total_volume': 15035890, 'high_24h': 48814, 'low_24h': 47152, 'price_change_24h': 1269.04, 'price_change_percentage_24h': 2.69139, 'market_cap_change_24h': 54270600, 'market_cap_change_percentage_24h': 2.88573, 'circulating_supply': 39906.36705999, 'total_supply': 39906.36705999, 'max_supply': 39906.36705999, 'ath': 69325, 'ath_change_percentage': -30.05912, 'ath_date': '2021-05-10T02:33:06.038Z', 'atl': 11209.02, 'atl_change_percentage': 332.5673, 'atl_date': '2020-10-12T03:56:16.768Z', 'roi': None, 'last_updated': '2021-09-18T18:52:03.742Z'}]

input- 1
output- [{'id': 'huobi-btc', 'symbol': 'hbtc', 'name': 'Huobi BTC', 'image': 'https://assets.coingecko.com/coins/images/12407/large/Unknown-5.png?1599624896', 'current_price': 48360, 'market_cap': 1929855749, 'market_cap_rank': 72, 'fully_diluted_valuation': 1929855749, 'total_volume': 15016424, 'high_24h': 48814, 'low_24h': 47164, 'price_change_24h': 1075.58, 'price_change_percentage_24h': 2.27472, 'market_cap_change_24h': 42922479, 'market_cap_change_percentage_24h': 2.27472, 'circulating_supply': 39906.36705999, 'total_supply': 39906.36705999, 'max_supply': 39906.36705999, 'ath': 69325, 'ath_change_percentage': -30.15357, 'ath_date': '2021-05-10T02:33:06.038Z', 'atl': 11209.02, 'atl_change_percentage': 331.98318, 'atl_date': '2020-10-12T03:56:16.768Z', 'roi': None, 'last_updated': '2021-09-18T19:16:00.574Z'}]