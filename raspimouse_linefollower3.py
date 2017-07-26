#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time # sleepのためのモジュールをインポート

# デバイスファイルからセンサ値を取得する関数を用意
def get_line_sensor_data():
    with open('/dev/rtlightsensor0','r') as f:
        return map(int, f.readline().split())

# デバイスファイルを通してモータの回転角度を指定する関数を用意
def set_motor_speed(left, right):
    with open('/dev/rtmotor_raw_l0','w') as lf, open('/dev/rtmotor_raw_r0','w') as rf:
        lf.write(str(int(left)))
        rf.write(str(int(right)))

# デバイスファイルからモータの電源をON/OFFする関数を用意
def set_motor_power(mode):
    with open('/dev/rtmotoren0','w') as f:
        f.write('1' if mode else '0')

# スイッチの入力データを返す関数を用意
def get_switch_input(swnum):
    with open('/dev/rtswitch'+str(swnum),'r') as f:
        return not(int(f.readline()))

if __name__ == '__main__':
    while not get_switch_input(False): # SW0が押されるまで待機
        print("ready")
        time.sleep(0.1)
    set_motor_power(True)
    while not get_switch_input(True): # SW1が押されたら止める
        left_end, left, right, right_end = get_line_sensor_data()
        print(left, right)
        diff = (left - right)/10
        print(diff)
        set_motor_speed(100+diff, 100-diff)
        time.sleep(0.1) # 0.1秒毎にセンサ値とモータの回転角度を更新
    set_motor_power(false)
