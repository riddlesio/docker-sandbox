# -*- coding: utf-8 -*-
# Python3.4*

import fileinput
import random

if __name__ == '__main__':
    for line in fileinput.input():
        stripped = line.strip()
        if len(stripped) == 0:
            continue
            
        words = stripped.split(' ')
        if words[0] != 'action':
            continue

        move = random.choice(['rock', 'paper', 'scissors'])
        print(move)
