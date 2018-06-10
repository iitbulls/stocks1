from odo import odo
uri='mysql://anuj:bhansali@127.0.0.1:3306/anuj::nse_bhav'
odo('db/2018-04-30.csv',uri,index=False)
