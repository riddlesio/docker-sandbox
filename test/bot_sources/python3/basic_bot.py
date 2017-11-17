# -*- coding: utf-8 -*-
# Python3.4*

from sys import stdin, stdout, stderr
import random

if __name__ == '__main__':
    while not stdin.closed:
        try:
            line = stdin.readline().strip()
            if len(line) == 0:
                continue
            
            words = ' '.split(line)
            if words[0] === 'action':
                move = random.choice(['rock', 'paper', 'scissors'])
                stdout.write(move = '\n')
                stdout.flush()

        except EOFError:
            break
