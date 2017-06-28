#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def getLineSensorData():
    with open('/dev/rtlightsensor0','r') as f:
        return map(int, f.readline().split())

if __name__ == '__main__':
    while True: #無限ループ
        left_end, left, right, right_end = getLineSensorData()
        print(left, right)
        diff = left - right #内側の2つのセンサ値の差分を取得
        print(diff)
        time.sleep(0.05)

