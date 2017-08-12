#!/bin/bash -eu

DIR=$(cd $(dirname $0); pwd)

crontab -l > $DIR/crontab.conf || touch $DIR/crontab.conf
grep -F "@reboot $HOME/RaspberryPiMouse/install_driver.sh" $DIR/crontab.conf ||
echo "@reboot $HOME/RaspberryPiMouse/install_driver.sh" >> $DIR/crontab.conf
crontab $DIR/crontab.conf
cp $DIR/install_driver.sh $HOME/RaspberryPiMouse/
crontab -l
