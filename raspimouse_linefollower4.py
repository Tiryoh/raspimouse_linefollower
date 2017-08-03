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

# センサ値を正規化するための関数を用意
def normalize(v, rng):
    return (v - rng[0]) / (rng[1] - rng[0])

# センサの値の範囲
left_end_range  = (240, 640)
left_range      = (650, 1350)
right_range     = (550, 1400)
right_end_range = (500, 1600)

if __name__ == '__main__':
    while not get_switch_input(0): # SW0が押されるまで待機
        print("ready")
        time.sleep(0.1)
    set_motor_power(True)
    while not get_switch_input(1): # SW1が押されたら止める
        # センサ値を取得
        left_end, left, right, right_end = get_line_sensor_data()
        # 内側の2つセンサ値を校正・比較
        diff_in = normalize(left, left_range) - normalize(right, right_range)
        # 外側の2つセンサ値を校正・比較
        diff_out = normalize(left_end, left_end_range) - normalize(right_end, right_end_range)
        # 校正したセンサ値を合算
        diff = diff_in/2 + diff_out
        print(diff_in, diff_out)
        set_motor_speed(100*(1+diff), 100*(1-diff))
        time.sleep(0.1) # 0.1秒毎にセンサ値とモータの回転角度を更新
    set_motor_power(False)
