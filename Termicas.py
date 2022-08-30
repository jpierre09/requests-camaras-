############# Import Libraries
import requests
from requests.auth import HTTPDigestAuth
from datetime import datetime
import os
import json
from login import *

################### By: Faiber Salazar ##################

############# Storage Path

path = '/var/ftp/upload/'
path_ultima = '/var/www/ultimasFotosCamaras/ultimacam_termica_'
termicas = json.load(open('/home/produccion/script/camaras/json/Termicas.json'))['Termicas']

############# Getting Image

for termica in termicas:

    fecha_actual  = datetime.now()
    fecha_archivo = fecha_actual.strftime("%y-%m-%d_%H-%M-%S")
    fecha_carpeta = fecha_actual.strftime("%Y-%m-%d")

    carpeta = path+termica["ruta"]+fecha_carpeta+'/'
    print(termica['link'])
    try:
        r = requests.get(termica['link'], auth=HTTPDigestAuth(FlirUs, FlirPass), timeout = 10)
    except:
        print("falle")
        continue
    print(r.status_code)
    if r.status_code != 200:
        continue
    with open(path_ultima+termica['ultima']+'.jpg', 'wb') as ultima:
        ultima.write(r.content)
    try:
        os.mkdir(carpeta)
    except:
        pass
    try:
        with open(carpeta+'image'+fecha_archivo+'.jpg', 'wb') as imagen:
            imagen.write(r.content)
    except:
        pass