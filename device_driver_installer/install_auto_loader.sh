#!/bin/bash -eu

# MIT License (C) 2017 Tiryoh<tiryoh@gmail.com>
# https://tiryoh.mit-license.org

[ -z $(uname -m | grep armv7l) ] && { echo "Run this script on Raspberry Pi"; exit 0; }
[ -d $HOME/RaspberryPiMouse ] || { echo "Download RaspberryPiMouse driver on your home directory."; exit 0; }

DIR=$(cd $(dirname $0); pwd)

sudo crontab -l > $DIR/crontab.conf || touch $DIR/crontab.conf
grep -F "@reboot $HOME/RaspberryPiMouse/install_driver.sh" $DIR/crontab.conf ||
echo "@reboot $HOME/RaspberryPiMouse/install_driver.sh" >> $DIR/crontab.conf
sudo crontab $DIR/crontab.conf
sed -e "s%\$HOME%$HOME%g" $DIR/install_driver.sh > $HOME/RaspberryPiMouse/install_driver.sh
chmod +x $HOME/RaspberryPiMouse/install_driver.sh
sudo crontab -l
