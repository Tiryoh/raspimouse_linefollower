#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def getLineSensorData():
    with open('/dev/rtlightsensor0','r') as f:
        return map(int, f.readline().split())

def setMotorSpeed(left, right, time):
    with open('/dev/rtmotor0','w') as f:
        f.write("%d %d %d" % (left, right, time))

def setMotorPower(mode):
    with open('/dev/rtmotoren0','w') as f:
        f.write('1' if mode else '0')

if __name__ == '__main__':
    setMotorPower(True)
    for i in range(0,50): #一定時間後に止めたいのでwhileではなくこちらで
        left_end, left, right, right_end = getLineSensorData()
        print(left, right)
        diff = (left - right)/10
        print(diff)
        setMotorSpeed(200+diff, 200-diff, 50)
        time.sleep(0.05) #スムーズに走らない場合はこの行を消す
    setMotorPower(False)

