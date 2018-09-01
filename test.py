import pandas as pd
from sqlalchemy import create_engine
import os
cnx = create_engine('mysql+pymysql://anuj:bhansali@127.0.0.1:3306/anuj', echo=False)
dir=os.listdir('db')
for r in dir:
   df=pd.read_csv('db/%s'%r)
   df.to_sql(name='nse_bhav', con=cnx, if_exists = 'append', index=False)

