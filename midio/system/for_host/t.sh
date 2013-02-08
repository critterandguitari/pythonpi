#!/bin/bash 
while : 
do 
    clear
    sudo mkdir /media/usbstick
    sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /media/usbstick
    cd /media/usbstick/pythonpi/midio/system/web
    ./run.sh &
    cd ../
    sudo python main.py
    cd ~
    clear
    echo "Stopping web server..."
    sudo killall -w python
    echo "Unmounting USB drive..."
    sudo umount /media/usbstick
    python wait.py
done
