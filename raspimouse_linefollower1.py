#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time # sleepのためのモジュールをインポート

# デバイスファイルからセンサ値を取得する関数を用意
def get_line_sensor_data():
    with open('./dev/rtlightsensor0','r') as f: # '/dev/rtlightsensor0'を開く
        raw_data = f.readline() # 文字列を1行読み取り
        list_data = raw_data.split() # スペースで文字列を分割
        return map(int, list_data) # 文字列を数値に変換したリストを返す

if __name__ == '__main__':
    while True: # Ctrl+Cで止めるまで無限ループ
        left_end, left, right, right_end = get_line_sensor_data() # 4つの変数にセンサ値を代入
        print(left_end, left, right, right_end) # 変数に代入された値を確認
        time.sleep(0.1) # 0.1秒毎にループを繰り返す
