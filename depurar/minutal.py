import os, fnmatch
from glob import glob
from datetime import datetime
import numpy as np

################### Author: Faiber Salazar ##################
today       = datetime.today().strftime('%Y-%m-%d')
today_short = datetime.today().strftime('%y-%m-%d')
############# Base Path
basepath   = '/var/ftp/upload/camara_drenaje_urbano_monterrey'
camspath   = f'{basepath}/{today}/*'
temppath   = f'{basepath}/temporal/'
camlist    = np.sort(glob(camspath))
firsthour  = camlist[0][-21:-19]
lasthour   = camlist[-1][-21:-19]
rangehour  = np.arange(int(firsthour), int(lasthour)+1)
print(rangehour)

for hour in rangehour:
    hour = "{:02d}".format(hour)
    for minute in range(0, 60):
        minute     = "{:02d}".format(minute)
        camsminute = f'{basepath}/{today}/image{today_short}_{hour}-{minute}*'
        print(camsminute)
        while len(glob(camsminute)) > 1:
            print(len(glob(camsminute)))
            os.system(f'rm {glob(camsminute)[0]}')
            