#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:40:38 2022

@author: jameschok
"""

with open('day05.txt', 'r') as file:
    lines = file.readlines()
    
    
stack = []
moves = []
is_stack = True

for line in lines:
    cleaned_line = line.replace('\n', '')
    
    if is_stack:
        is_stack = line == ''
        continue
        
    if is_stack:
        stack.append(cleaned_line)
    else:
        moves.append(cleaned_line)
    
print(stack)
print(moves)
    