import pandas as pd
from odo import odo
import numpy as np
uri='mysql://anuj:bhansali@127.0.0.1:3306/anuj::nse_bhav'
df=odo(uri,pd.DataFrame)
#start = datetime.datetime(2016,1,1)
#end = datetime.date.today()
print (list(df))
print (df.head)

#t["7d"] = np.round(df['close'].rolling(window=7).mean(), 2)
#sp500['252d'] = np.round(sp500['Close'].rolling(window=252).mean(), 2)



