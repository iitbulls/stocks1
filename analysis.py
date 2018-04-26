import pandas as pd
from odo import odo

uri='mysql://anuj:bhansali@127.0.0.1:3306/anuj::nse_bhav'
df=odo(uri,pd.DataFrame)
print (list(df))
print (df.head)
start = datetime.datetime(2016,1,1)
end = datetime.date.today()




