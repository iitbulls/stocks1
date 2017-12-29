import pandas as pd
import os
for filename in os.listdir('db'):
    df= pd.read_csv('db/%s'%filename)
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], infer_datetime_format=True)
    df.to_csv('db/%s'%filename,index=False)