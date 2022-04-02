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
    total_computations = 100
    custom_bar = ProgressBar(total_computations, bar_width=50, char='=', head='>', todo=' ',
                             spinner=True, percentage=True)
    
    for _ in range(total_computations):
        custom_bar()
        sleep(0.1)
    pass

if __name__ == '__main__':
    test()
