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
    total_computations = 500
    computation_time = 0.005
    test_default(total_computations, computation_time)
    test_custom(total_computations, computation_time)
    test_preset(total_computations, computation_time)
    test_overhead(total_computations, computation_time)

def run(bar, total_computations, computation_time):
    for _ in range(total_computations):
        bar()
        sleep(computation_time)

def test_default(total_computations, computation_time):
    print('default')
    bar1 = ProgressBar(total_computations)
    run(bar1, total_computations, computation_time)

    print('spinner off, basic coloring, custom characters')
    bar2 = ProgressBar(total_computations, spinner=False, color='green', bg_color='yellow', head='H')
    run(bar2, total_computations, computation_time)

def test_custom(total_computations, computation_time):
    bar = ProgressBar(total_computations, braces='{}')
    
    bar.set_char('>', 'magenta', 'black')
    bar.set_head('O', bg_color='black')
    bar.set_todo(color='magenta')
    bar.set_char('*', 'blue', 'white')

    bar.style('bold', 'base')
    bar.style('faint', 'todo')

    bar.set_char(color='magenta', bg_color='black')
    bar.set_braces(color='bright_magenta')

    print('individual character customization')
    run(bar, total_computations, computation_time)

def test_preset(total_computations, computation_time):
    bar1 = ProgressBar(total_computations, preset = 'minimal')
    print('preset: minimal')
    run(bar1, total_computations, computation_time)

    bar2 = ProgressBar(total_computations, preset = 'oldschool')
    print('preset: oldschool')
    run(bar2, total_computations, computation_time)

def test_overhead(total_computations, computation_time):

    def run_with(total_computations: int, computation_time: float) -> float:
        start = time()
        bar = ProgressBar(total_computations)
        for _ in range(total_computations):
            bar()
            sleep(computation_time)
        end = time()
        return end - start
    
    def run_without(total_computations: int, computation_time: float) -> float:
        start = time()
        # place for bar initialization
        for _ in range(total_computations):
            # place for bar updating
            sleep(computation_time)
        end = time()
        return end - start

    print('calculating overhead...')
    overhead = run_with(total_computations, computation_time) - run_without(total_computations, computation_time)    
    print(f'{overhead = :.4f} sec')


if __name__ == '__main__':
    main()
