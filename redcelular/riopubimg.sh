#!/bin/bash

date
echo $date

TODAY=$(date +%Y-%m-%d)
echo 'La fecha actual es: '$TODAY

#appdir=`dirname $0`
#logfile=$appdir/LogRioGetImages.log
#lockfile=$appdir/LckRioGetImages.lck
#pid=$$

echo $appdir

#function GetImage {
cd /home/produccion/script/camaras/redcelular/

##### List last image
lastnivelprimavera=`ls -t1 /var/ftp/upload/camara_nivel_primavera/$TODAY | head -n2 | tail -n1`
lastnivelplebicito=`ls -t1 /var/ftp/upload/camara_nivel_plebicito/$TODAY | head -n2 | tail -n1`
lastdrenajemonterrey=`ls -t1 /var/ftp/upload/camara_drenaje_urbano_monterrey/$TODAY | head -n2 | tail -n1`

##### Copying to /var/www/
cp "/var/ftp/upload/camara_nivel_primavera/"$TODAY"/"${lastnivelprimavera} "/var/www/ultimasFotosCamaras/ultimacam_nivel_primavera.jpg"
cp "/var/ftp/upload/camara_nivel_plebicito/"$TODAY"/"${lastnivelplebicito} "/var/www/ultimasFotosCamaras/ultimacam_nivel_plebicito.jpg"
cp "/var/ftp/upload/camara_drenaje_urbano_monterrey/"$TODAY"/"${lastdrenajemonterrey} "/var/www/ultimasFotosCamaras/ultimacam_drenaje_urbano_monterrey.jpg"
#}


#(
#        if flock -n 201; then
#                cd $appdir
#                GetImage
#                echo $appdir $lockfile
#                #rm -f $lockfile
#        else
#            	echo "`date` [$pid] - Script is already executing. Exiting now." >> $logfile
#        fi
#) 201>$lockfile

#exit 0
