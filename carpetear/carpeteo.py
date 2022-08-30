import os, fnmatch
from glob import glob
from datetime import datetime
import sys
# import module sys to get the type of exception


################### Author: Faiber Salazar ##################

############# Base Path

basepath   = '/var/ftp/upload'
camspath   = f"{basepath}/cam*"
folderlist = glob(camspath)

for folder in folderlist:
    while True:
        uncarpetedfiles = glob(f"{folder}/image*.jpg")
        if len(uncarpetedfiles) > 0:
            print(f"{folder}: {len(uncarpetedfiles)}")
            date    = uncarpetedfiles[0].split('/')[-1][5:13]
            datestr = datetime.strptime(date, '%y-%m-%d').strftime('%Y-%m-%d')
            print(f"{datestr}")
            try:
                os.mkdir(f"{folder}/{datestr}")
            except:
                pass
            old = f"{folder}/image{date}*.jpg"
            new = f"{folder}/{datestr}/"
            os.system(f"mv -f {old} {new}")          
        else: break
