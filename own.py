from urlfetch import fetch
import pandas as pd
from io import BytesIO
from zipfile import ZipFile
import datetime
import time
import os
from odo import odo
uri='mysql://anuj:bhansali@127.0.0.1:3306/anuj::nse_bhav'

def bhav(dt):
    MMM = dt.strftime("%b").upper()
    yyyy = dt.strftime("%Y")
    file = dt.strftime("%d%b%Y").upper()
    if dt.weekday()<5:
        try:
            url = fetch("https://www.nseindia.com/content/historical/EQUITIES/%s/%s/cm%sbhav.csv.zip"%(yyyy,MMM,file),randua=True)
            if url.status==200:
                #Download Zipfile and create pandas DataFrame
                zf = ZipFile(BytesIO(url.content))
                fp=zf.namelist()[0]
                df = pd.read_csv(zf.open(fp))
                del df['Unnamed: 13']
                df=df[df["SERIES"].isin(["EQ"])]
                df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], infer_datetime_format=True)# to covert date from string to date and change format to accept SQL
                df.to_csv('db/%s.csv'%dt, index=False)
                odo('db/%s.csv' %dt, uri)
                time.sleep(1)
                print(dt)
                time.sleep(2)
            else:
                pass
        except Exception:
            pass
    else:
        print("Weekend")

def daterange(start_date,end_date):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1):
            yield start_date + datetime.timedelta(n)
    else:
        for n in range((start_date-end_date).days+1):
            yield start_date-datetime.timedelta(n)

def maxdt():
    list = (os.listdir('db'))
    newlist=[]
    for i in list:
        x=i[:-4]
        newlist.append(x)
    return (max(newlist))

start =datetime.datetime.strptime(maxdt(),'%Y-%m-%d').date()
end = datetime.datetime.now().date()
for a in daterange( start, end ):
    bhav(a)

