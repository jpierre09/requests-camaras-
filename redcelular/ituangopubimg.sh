#!/bin/bash

date
appdir=`dirname $0`
logfile=$appdir/LogRioGetImages.log
lockfile=$appdir/LckRioGetImages.lck
pid=$$

echo $appdir

function GetImage {
cd /home/produccion/script/camaras/redcelular/

##### List last image
lastcamituangodescarga=`ls -t1 /var/ftp/upload/camara_ituango_descarga/ | head -n2 | tail -n1`
lastcamituangoembalse=`ls -t1 /var/ftp/upload/camara_ituango_embalse/ | head -n2 | tail -n1`
lastcamituangosubestacion=`ls -t1 /var/ftp/upload/camara_ituango_sub_estacion_500/ | head -n2 | tail -n1`


##### Copying to /var/www/
cp "/var/ftp/upload/camara_ituango_descarga/"${lastcamituangodescarga} "/var/www/ultimasFotosCamaras/ultimacam_ituango_descarga.jpg"
cp "/var/ftp/upload/camara_ituango_embalse/"${lastcamituangoembalse} "/var/www/ultimasFotosCamaras/ultimacam_ituango_embalse.jpg"
cp "/var/ftp/upload/camara_ituango_sub_estacion_500/"${lastcamituangosubestacion} "/var/www/ultimasFotosCamaras/ultimacam_ituango_sub_estacion_500.jpg"

}


(
        if flock -n 201; then
                cd $appdir
                GetImage
                echo $appdir $lockfile
                rm -f $lockfile
        else
            	echo "`date` [$pid] - Script is already executing. Exiting now." >> $logfile
        fi
) 201>$lockfile

exit 0
