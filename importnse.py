from nsepy.history import get_price_list
import datetime
import time
def download_bhav(y,m,d):
    prices = get_price_list(dt=datetime.date(y,m,d))
    prices.to_csv('db/test2.csv',index=False)
    time.sleep(7)
download_bhav(2017,9,15)

