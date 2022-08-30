import os, json
from glob import glob
from datetime import datetime
import numpy as np

################### Author: Faiber Salazar ##################
today       = datetime.today().strftime('%Y-%m-%d')
############# Base Path #############
basepath   = '/var/ftp/upload'
ultimapath = '/var/www/ultimasFotosCamaras/ultimacam_'
redcelular = json.load(open('/home/produccion/script/camaras/json/RedCelular.json'))

for camara in redcelular:
    try:
        camspath   = f'{basepath}/{camara["ruta"]}/image*'
        camlist    = np.sort(glob(camspath))
        ultima = camlist[-1]
        if ultima != camara["log"]:
            os.system(f'cp {ultima} {ultimapath}{camara["ultima"]}.jpg')
            camara["log"] = ultima
            print(f'{camara["ultima"]}: {ultima.split("/")[-1]}')
        else:
            print(f'{camara["ultima"]}: Actualizada')
    except:
        camspath   = f'{basepath}/{camara["ruta"]}/{today}/image*'
        camlist    = np.sort(glob(camspath))
        if len(camlist) == 0:
            print(f'{camara["ultima"]}: No hay imagenes para hoy')
            continue
        ultima = camlist[-1]
        if ultima != camara["log"]:
            os.system(f'cp {ultima} {ultimapath}{camara["ultima"]}.jpg')
            camara["log"] = ultima
            print(f'{camara["ultima"]}: {ultima.split("/")[-1]}')
        else:
            print(f'{camara["ultima"]}: Actualizada')
    
json.dump(redcelular,open('/home/produccion/script/camaras/json/RedCelular.json','w'), indent=4)
