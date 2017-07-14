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
        lf.write(str(left))
        rf.write(str(right))

# デバイスファイルからモータの電源をON/OFFする関数を用意
def set_motor_power(mode):
    with open('/dev/rtmotoren0','w') as f:
        f.write('1' if mode else '0')

if __name__ == '__main__':
    set_motor_power(True)
    for i in range(10): # 一定時間後に止めたいのでwhileではなく回数指定
        left_end, left, right, right_end = get_line_sensor_data() # 4つの変数のセンサ値を代入
        print(left, right) # 変数に代入された値を確認
        set_motor_speed(100, 100) # ステッピングモータを回転
        time.sleep(0.1) # 0.1秒毎にセンサ値とモータの回転角度を更新
    set_motor_power(False)
