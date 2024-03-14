# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:23:59 2024

@author: student
"""

import random

n = int(input("請輸入要抽取的數字個數 n："))
a = int(input("請輸入數字範圍的起始值 a："))
b = int(input("請輸入數字範圍的結束值 b："))

random_numbers = random.sample(range(a, b + 1), n)

unique_numbers = list(set(random_numbers))

unique_numbers.sort(reverse=True)

print("隨機抽取並排序後的數字為：", unique_numbers)