#!/bin/bash

date
appdir=`dirname $0`
#logfile=$appdir/LogDeslizamientoGetImages.log
#lockfile=$appdir/LckDeslizamientoGetImages.lck
pid=$$

echo $appdir

#function GetImage {
cd /home/produccion/script/camaras/redcelular/

#####  List last image

lastcamdeslizamientopalmitas=`ls -t1 /var/ftp/upload/camara_deslizamiento_palmitas/ | head -n2 | tail -n1`
lastcamdeslizamientolassalinas=`ls -t1 /var/ftp/upload/camara_deslizamiento_las_salinas_caldas/ | head -n2 | tail -n1`
lastcamdeslizamientojerico=`ls -t1 /var/ftp/upload/camara_deslizamiento_jerico/ | head -n2 | tail -n1`
lastcamdeslizamientojerico2=`ls -t1 /var/ftp/upload/camara_deslizamiento_jerico_2/ | head -n2 | tail -n1`
lastcamdeslizamientojerico_3=`ls -t1 /var/ftp/upload/camara_deslizamiento_jerico3/ | head -n2 | tail -n1`
lastcamdeslizamientolavaleria=`ls -t1 /var/ftp/upload/camara_deslizamiento_la-valeria/ | head -n2 | tail -n1`
lastcamdeslizamientolaprimavera=`ls -t1 /var/ftp/upload/camara_deslizamiento_la_primavera/ | head -n2 | tail -n1`

##### Copying to /var/www/
cp "/var/ftp/upload/camara_deslizamiento_palmitas/"${lastcamdeslizamientopalmitas} "/var/www/ultimasFotosCamaras/ultimacam_deslizamiento_palmitas.jpg"
cp "/var/ftp/upload/camara_deslizamiento_las_salinas_caldas/"${lastcamdeslizamientolasalinas} "/var/www/ultimasFotosCamaras/ultimacam_deslizamiento_las_salinas_caldas.jpg"
cp "/var/ftp/upload/camara_deslizamiento_jerico/"${lastcamdeslizamientojerico} "/var/www/ultimasFotosCamaras/ultimacam_deslizamiento_jerico.jpg"
cp "/var/ftp/upload/camara_deslizamiento_jerico_2/"${lastcamdeslizamientojerico2} "/var/www/ultimasFotosCamaras/ultimacam_deslizamiento_jerico_2.jpg"
cp "/var/ftp/upload/camara_deslizamiento_jerico3/"${lastcamdeslizamientojerico_3} "/var/www/ultimasFotosCamaras/ultimacam_deslizamiento_jerico_3.jpg"
cp "/var/ftp/upload/camara_deslizamiento_la-valeria/"${lastcamdeslizamientolavaleria} "/var/www/ultimasFotosCamaras/ultimacam_deslizamiento_la-valeria.jpg"
cp "/var/ftp/upload/camara_deslizamiento_la_primavera/"${lastcamdeslizamientolaprimavera} "/var/www/ultimasFotosCamaras/ultimacam_deslizamiento_la_primavera.jpg"

#mogrify -set comment 'Extraneous bytes removed' /var/www/ultimasFotosCamaras/ultimacam_deslizamiento_*.jpg

#}


#(
#        if flock -n 201; then
#                cd $appdir
#                GetImage
#                echo $appdir $lockfile
#                rm -f $lockfile
#        else
#           	echo "`date` [$pid] - Script is already executing. Exiting now." >> $logfile
#        fi
#) 201>$lockfile

#exit 0
