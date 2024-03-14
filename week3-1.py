# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
lower_to_upper_dict = {chr(i): chr(i).upper() for i in range(ord('a'), ord('z')+1)}

input_char = input("請輸入小寫英文字母：")

if input_char in lower_to_upper_dict:
    result = lower_to_upper_dict[input_char]
    print("轉換後的大寫字母為：", result)
else:
    print("請輸入正確的小寫英文字母！")