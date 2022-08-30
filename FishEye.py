############# Import Libraries
import requests
from datetime import datetime
import os
import json
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO


################### By: Faiber Salazar ##################

############# Storage Path

path = '/var/ftp/upload/'
path_ultima = '/var/www/ultimasFotosCamaras/ultimacam_'
fishs = json.load(open('/home/produccion/script/camaras/json/FishEye.json'))['FishEye']

############# Getting Image

for fish in fishs:

    fecha_actual  = datetime.now()
    fecha_archivo = fecha_actual.strftime("%y-%m-%d_%H-%M-%S")
    fecha_carpeta = fecha_actual.strftime("%Y-%m-%d")
    fecha_banner  = fecha_actual.strftime("%Y/%m/%d %H:%M:%S")

    carpeta = path+fish["ruta"]+fecha_carpeta+'/'
    print(fish['ip'],fish['ultima'])
    try:
        r = requests.get('http://'+fish['ip']+'/PictureCatch.cgi?username=root&password=CamPass.21&channel=1', timeout = 10)
    except:
        continue
    if r.status_code != 200:
        continue
    im = Image.open(BytesIO(r.content))
    out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    draw = ImageDraw.Draw(out)
    font = ImageFont.truetype("arial.ttf", 75)
    draw.text((50, 0), "www.siata.gov.co", fill='white', font=font)
    draw.text((2150, 0), fecha_banner, fill='white', font=font)
    out.save(path_ultima+fish['ultima']+'.jpg')
    try:
        os.mkdir(carpeta)
    except:
        pass
    try:
        with open(carpeta+'image'+fecha_archivo+'.jpg', 'wb') as imagen:
            imagen.write(r.content)
    except:
        pass
    # with open(path_ultima+fish['ultima']+'.jpg', 'wb') as ultima:
    #     ultima.write(r.content)