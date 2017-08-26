#!/bin/bash -eu

# MIT License (C) 2017 Tiryoh<tiryoh@gmail.com>
# https://tiryoh.mit-license.org

[ -z $(uname -m | grep armv7l) ] && { echo "Run this script on Raspberry Pi"; exit 0; }

DIR=$(cd $(dirname $0); pwd)

crontab -l > $DIR/crontab.conf || touch $DIR/crontab.conf
grep -F "@reboot $HOME/RaspberryPiMouse/install_driver.sh" $DIR/crontab.conf ||
echo "@reboot $HOME/RaspberryPiMouse/install_driver.sh" >> $DIR/crontab.conf
crontab $DIR/crontab.conf
cp $DIR/install_driver.sh $HOME/RaspberryPiMouse/
crontab -l
