#!/usr/bin/env python3
# -*- coding=utf-8 -*-

i = 0
for x in range(1000,2001):
    if x % 4 == 0 and x % 100 != 0: #判断x能被4整除但不能被100整除
        i = i + 1
        print(x)
    elif x % 400 == 0:              #判断x能被100整除且能被400整除
        i = i + 1
        print(x)

print('i = ',i)
