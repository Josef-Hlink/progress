#!/usr/bin/env python3
"""
for handling a spinner object
---
Initial commit: 08-05-2022
Author: J.D. Hamelink
"""

class Spinner:
    def __init__(self, name: str = 'default'):
        self.frames = self._get_frames(name)
    
    def __call__(self, i: int = 0):
        return self.frames[i%len(self.frames)]

    def _get_frames(self, name: str = None) -> list[str]:
        self.dictionary = {
            '':                         [''],
            'default':                  ['|', '/', '-', '\\'],

            'quarter':                  ['▘', '▝', '▗', '▖'],
            'inv_quarter':              ['▟', '▙', '▛', '▜'],
            'half_box':                 ['◧', '◩', '◨', '◪'],
            'clock':                    ['◴', '◷', '◶', '◵'],
            'triangle_corners':         ['◸', '◹', '◿', '◺'],
            'triangle_corners_filled':  ['◤', '◥', '◢', '◣'],
            'quarter_box':              ['◰', '◳', '◲', '◱'],

            'slider':                   ['╵', '╹', '╿', '╽', '╻', '╷', '╻', '╽', '╿', '╹'],
            'horizontal_slider':        ['╴', '╸', '╾', '╼', '╺', '╶', '╺', '╼', '╾', '╸'],

            'cross_slider':             ['╀', '╄', '┾', '╆', '╁', '╅', '┽', '╃'],
            'dynamic_quarter':          ['▘', '▀', '▝', '▐', '▗', '▄', '▖', '▌'],
            'horizontal_hourglass':     ['⧔', '⧑', '⧓', '⧒', '⧕', '⧒', '⧓', '⧑'],

            'quarter_circle':           ['◜ ', ' ◝', ' ◞', '◟ '],

            'wheel':                    ['⨁', '⨂']
        }
        try:
            return self.dictionary[name]
        except KeyError:
            raise ValueError(f'Invalid spinner name "{name}", take a look at the Spinner().help() method')
    
    def help(self) -> None:
        print(f'These are all of the valid spinner names:\n\n{list(self.dictionary.keys())}')


if __name__ == '__main__':
    Spinner().help()
