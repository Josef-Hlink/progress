#!/usr/bin/env python3
"""
testing suite script for a python progress bar
---
Initial commit: 01-04-2022
Author: J.D. Hamelink
"""

from progress import ProgressBar
from time import sleep, time

def main():
    test()
    #test_overhead()

def test_overhead():

    def run_with(total_computations: int, computation_time: float) -> float:
        start = time()
        custom_bar = ProgressBar(total_computations, bar_width=50, char='=', head='>', todo=' ',
                                 spinner=True, percentage=True)
        for _ in range(total_computations):
            custom_bar()
            sleep(computation_time)
        end = time()
        return end - start
    
    def run_without(total_computations: int, computation_time: float) -> float:
        start = time()
        for _ in range(total_computations):
            sleep(computation_time)
        end = time()
        return end - start

    total_computations = 500
    computation_time = 0.01
    overhead = run_with(total_computations, computation_time) - run_without(total_computations, computation_time)    
    print(f'{overhead = :.2f} sec')


def test():
    total_computations = 500
    computation_time = 0.01
    custom_bar = ProgressBar(total_computations)
    
    custom_bar.set_char(color='bright_white', bg_color='blue')
    custom_bar.set_head('-', 'bright_white', 'bright_cyan')
    custom_bar.set_todo('-', bg_color='bright_cyan')
    
    custom_bar.style('bold', 'base')
    custom_bar.style('blink', 'todo')

    for _ in range(total_computations):
        custom_bar()
        sleep(computation_time)


if __name__ == '__main__':
    main()
