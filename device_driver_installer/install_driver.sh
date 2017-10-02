#!/bin/bash -eu

# MIT License (C) 2017 Tiryoh<tiryoh@gmail.com>
# https://tiryoh.mit-license.org

[ -z $(uname -m | grep armv7l) ] && { echo "Run this script on Raspberry Pi"; exit 0; }

if [ -e $HOME/RaspberryPiMouse/src/drivers/rtmouse.ko ]; then
	DRIVER=$HOME/RaspberryPiMouse/src/drivers/rtmouse.ko
else
	DRIVER=$HOME/RaspberryPiMouse/lib/Pi2B+/`uname -r`/rtmouse.ko
fi

if [ -z $(whoami | grep root) ]; then
	sudo /sbin/insmod $DRIVER
	sleep 1
	[ -w /dev/rtled0 ] || sudo chmod 666 /dev/rt*
else
	/sbin/insmod $DRIVER
	sleep 1
	[ -w /dev/rtled0 ] || chmod 666 /dev/rt*
fi
echo 0 > /dev/rtmotoren0
