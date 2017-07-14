#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time # sleepのためのモジュールをインポート

# デバイスファイルからセンサ値を取得する関数を用意
def get_line_sensor_data():
    with open('/dev/rtlightsensor0','r') as f:
        return map(int, f.readline().split())

# スイッチの入力データを返す関数を用意
def get_switch_input(swnum):
    with open('/dev/rtswitch'+str(swnum),'r') as f:
        return not(int(f.readline()))

# デバイスファイルを通してモータの回転角度を指定する関数を用意
def set_motor_speed(left, right):
    with open('/dev/rtmotor_raw_l0','w') as lf, open('/dev/rtmotor_raw_r0','w') as rf:
        lf.write(str(int(left)))
        rf.write(str(int(right)))

# デバイスファイルからモータの電源をON/OFFする関数を用意
def set_motor_power(mode):
    with open('/dev/rtmotoren0','w') as f:
        f.write('1' if mode else '0')

# センサ値の値域が大きく異なる場合に補正するための関数を用意
def correct_seneor_value(current, old_min, old_max):
    return int((current - old_min) / float(old_max - old_min) * 100)

# センサの個体差補正用の変数宣言
left_end_min, left_end_max = 240, 640
left_min, left_max = 650, 1350
right_min, right_max = 550, 1400
right_end_min, right_end_max = 500, 1600

if __name__ == '__main__':
    while not get_switch_input(0): # SW0が押されるまで待機
        print("ready")
        time.sleep(0.1)
    set_motor_power(True)
    while not get_switch_input(1): # SW1が押されたら止める
        # センサ値を取得
        left_end, left, right, right_end = get_line_sensor_data()
        # 内側の2つセンサ値を補正・比較
        diff1 = correct_seneor_value(left, left_min, left_max) - correct_seneor_value(right, right_min, right_max)
        # 外側の2つセンサ値を補正・比較
        diff2 = correct_seneor_value(left_end, left_end_min, left_end_max) - correct_seneor_value(right_end, right_end_min, right_end_max)
        # 補正したセンサ値を合算
        diff = diff1 / 2 + diff2
        print(diff1, diff2)
        set_motor_speed(100+diff, 100-diff)
        time.sleep(0.1) # 0.1秒毎にセンサ値とモータの回転角度を更新
    set_motor_power(False)
