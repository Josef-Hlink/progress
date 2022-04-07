#!/usr/bin/env python3
"""
main script for a python progress bar
---
Initial commit: 01-04-2022
Author: J.D. Hamelink
"""

from progress import ProgressBar
from time import sleep

def test():
    total_computations = 500
    computation_time = 0.01

    custom_bar = ProgressBar(total_computations, bar_width=50, char='=', head='>', todo='-',
                             spinner=False, percentage=True)
    for _ in range(total_computations):
        custom_bar()
        sleep(computation_time) # dummy function

if __name__ == '__main__':
    test()
