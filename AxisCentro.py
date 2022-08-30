import requests
from requests.auth import HTTPDigestAuth
from datetime import date
from datetime import datetime
from login import *
import os
import json
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError

################### Author: Jean Pierre ##################

############# Storage Path

basepath = '/var/ftp/upload/'
path_ultima = '/var/www/ultimasFotosCamaras/ultimacam_'
axiscentro = json.load(open('/home/produccion/script/camaras/json/Centro.json'))['Axis']


############# Getting image & login & stocker
## format datetime dd-mm-yy H-M-S

for ax in axiscentro:

    fecha_actual = datetime.now()
    fh = fecha_actual.strftime('%y-%m-%d_%H-%M-%S')
    folder = fecha_actual.strftime('%Y-%m-%d')

    url = 'http://'+ax['ip']+'/axis-cgi/jpg/image.cgi?resolution=1280x720'
    try:
        r = requests.get(url, auth=HTTPDigestAuth(us, pa), timeout=5)
    except:
        continue

    if r.status_code != 200:
        continue

    try:
        os.mkdir(basepath+ax['ruta']+folder+'/')
    except:
        pass


    filename = 'image'+fh+'.jpg'
#    print(r.status_code)
    with open(path_ultima+ax['ultima']+'.jpg', 'wb') as out:
            out.write(r.content) 
    try:
        with open(basepath+ax['ruta']+folder+'/'+filename, 'wb') as out:
            out.write(r.content)       
    except:
        pass
############
