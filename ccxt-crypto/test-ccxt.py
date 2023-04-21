# source: https://pypi.org/project/ccxt/
import ccxt
print(ccxt.exchanges) # print a list of all available exchange classes
input("Hit 'Enter' to continue...")
doc = "https://pypi.org/project/ccxt/"
print("Go visit documentation at:", doc)
input("Hit 'Enter' to continue...")
hitbtc = ccxt.hitbtc({'verbose': True})
bitmex = ccxt.bitmex()
huobipro = ccxt.huobipro()

hitbtc_markets = hitbtc.load_markets()
input("Hit 'Enter' to display HitBTC markets...")
print(hitbtc.id, hitbtc_markets)
input("Hit 'Enter' to display BitMEX markets...")
print(bitmex.id, bitmex.load_markets())
input("Hit 'Enter' to display HuobiPro markets...")
print(huobipro.id, huobipro.load_markets())

input("Hit 'Enter' to display HitBTC order book...")
print(hitbtc.fetch_order_book(hitbtc.symbols[0]))
input("Hit 'Enter' to display BitMEX BTC/USD pair...")
print(bitmex.fetch_ticker('BTC/USD'))
input("Hit 'Enter' to display HuobiPro LTC/USDT pair...")
print(huobipro.fetch_trades('LTC/USDT'))

