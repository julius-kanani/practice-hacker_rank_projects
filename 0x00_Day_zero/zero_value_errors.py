#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:17:24 2022
Capture Exceptions. Zero division Error and ValueError.

@author: julius_kanani
"""

# Number of lines for input
lines = int(input())

for _ in range(lines):
    # get the values from input
    a, b = input().split()
    
    try:
        print(int(a)//int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)