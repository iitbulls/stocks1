from odo import odo
import os
import time
uri='mysql://anuj:bhansali@127.0.0.1:3306/anuj::nse_bhav'
for filename in os.listdir('db'):
    odo('db/%s'%filename, uri)
    time.sleep(1)
    print(filename)