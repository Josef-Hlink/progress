#!/usr/bin/env python3
"""
styling script for a python progress bar
---
Initial commit: 15-04-2022
Author: J.D. Hamelink
"""

import re # stripping styles from strings

class Style:
    def __init__(self):
        style_file = 'style.txt'
        self.c = self.load_base_colors(style_file)

    def set_color(self, color: str, char: str = None) -> str:
        """Set the color of a character (base, head, todo or brace)"""
        if color not in set(self.c.keys()):
            raise ValueError(f'Invalid color "{color}", look at the README to see all available colors') # TODO actually write README
        return getattr(self, color)(self.strip_fg_color(char))
    
    def set_bg_color(self, color: str, char: str = None):
        """Set the background color of a character (base, head, todo or brace)"""
        if color not in set(self.c.keys()):
            raise ValueError(f'Invalid background color "{color}", look at the README to see all available colors') # TODO actually write README
        bg_color = color+'_bg'
        return getattr(self, bg_color)(self.strip_bg_color(char))

    def get_original(self, string: str) -> str:
        """Remove all font effects and coloring from a string to get the original"""
        for color_code in re.findall('[0-5]|[349][0-7]|10[0-7]', string):   # 0-5, 30-37, 40-47, 90-97, 100-107
            string = string.replace(f'\033[{color_code}m', '')
        return string 
    
    def strip_all_colors(self, string: str) -> str:
        """Remove all coloring of a string"""
        for color_code in re.findall('0|[349][0-7]|10[0-7]', string):       # 0, 30-37, 40-47, 90-97, 100-107
            string = string.replace(f'\033[{color_code}m', '')
        return string
    
    def strip_fg_color(self, string: str) -> str:
        """Remove all foreground coloring of a string"""
        for color_code in re.findall('[39][0-7]', string):                  # 30-37, 90-97
            string = string.replace(f'\033[{color_code}m', '')
        return string
    
    def strip_bg_color(self, string: str) -> str:
        """Remove all background coloring of a string"""
        for color_code in re.findall('4[0-7]|10[0-7]', string):             # 40-47, 100-107
            string = string.replace(f'\033[{color_code}m', '')
        return string

    def load_base_colors(self, filename: str) -> dict:
        """Read all base color codes (just numbers) from given .txt file"""
        c = dict()

        # Add basic color numbers (fg and bg) to the color dict
        with open(filename) as f:
            f.readline()    # skip header
            for line in f.readlines():
                name, fg, bg = line.strip().split(',')
                c.update({name: (fg, bg)})
        
        # Add bright color numbers (fg and bg) to the color dict
        with open(filename) as f:
            f.readline()    # skip header
            for line in f.readlines():
                name, fg, bg = line.strip().split(',')
                b_name, b_fg, b_bg = 'bright_'+name, str(int(fg)+60), str(int(bg)+60)
                c.update({b_name: (b_fg, b_bg)})

        return c

    # font functions
    if True: # make block collapsable in an IDE
        def bold(self, string: str) -> str:
            return f'\033[1m{string}\033[0m'
        
        def faint(self, string: str) -> str:
            return f'\033[2m{string}\033[0m'
        
        def italic(self, string: str) -> str:
            return f'\033[3m{string}\033[0m'
        
        def underline(self, string: str) -> str:
            return f'\033[4m{string}\033[0m'

        def blink(self, string: str) -> str:
            return f'\033[5m{string}\033[0m'

    # fg coloring functions
    if True: # make block collapsable in an IDE
        def black(self, string: str) -> str:
            return f"\033[{self.c['black'][0]}m{string}\033[0m"

        def red(self, string: str) -> str:
            return f"\033[{self.c['red'][0]}m{string}\033[0m"

        def green(self, string: str) -> str:
            return f"\033[{self.c['green'][0]}m{string}\033[0m"

        def yellow(self, string: str) -> str:
            return f"\033[{self.c['yellow'][0]}m{string}\033[0m"

        def blue(self, string: str) -> str:
            return f"\033[{self.c['blue'][0]}m{string}\033[0m"

        def magenta(self, string: str) -> str:
            return f"\033[{self.c['magenta'][0]}m{string}\033[0m"

        def cyan(self, string: str) -> str:
            return f"\033[{self.c['cyan'][0]}m{string}\033[0m"

        def white(self, string: str) -> str:
            return f"\033[{self.c['white'][0]}m{string}\033[0m"

        def bright_black(self, string: str) -> str:
            return f"\033[{self.c['bright_black'][0]}m{string}\033[0m"

        def bright_red(self, string: str) -> str:
            return f"\033[{self.c['bright_red'][0]}m{string}\033[0m"

        def bright_green(self, string: str) -> str:
            return f"\033[{self.c['bright_green'][0]}m{string}\033[0m"

        def bright_yellow(self, string: str) -> str:
            return f"\033[{self.c['bright_yellow'][0]}m{string}\033[0m"

        def bright_blue(self, string: str) -> str:
            return f"\033[{self.c['bright_blue'][0]}m{string}\033[0m"

        def bright_magenta(self, string: str) -> str:
            return f"\033[{self.c['bright_magenta'][0]}m{string}\033[0m"

        def bright_cyan(self, string: str) -> str:
            return f"\033[{self.c['bright_cyan'][0]}m{string}\033[0m"

        def bright_white(self, string: str) -> str:
            return f"\033[{self.c['bright_white'][0]}m{string}\033[0m"

    # bg coloring functions
    if True: # make block collapsable in an IDE
        def black_bg(self, string: str) -> str:
            return f"\033[{self.c['black'][1]}m{string}\033[0m"

        def red_bg(self, string: str) -> str:
            return f"\033[{self.c['red'][1]}m{string}\033[0m"

        def green_bg(self, string: str) -> str:
            return f"\033[{self.c['green'][1]}m{string}\033[0m"

        def yellow_bg(self, string: str) -> str:
            return f"\033[{self.c['yellow'][1]}m{string}\033[0m"

        def blue_bg(self, string: str) -> str:
            return f"\033[{self.c['blue'][1]}m{string}\033[0m"

        def magenta_bg(self, string: str) -> str:
            return f"\033[{self.c['magenta'][1]}m{string}\033[0m"

        def cyan_bg(self, string: str) -> str:
            return f"\033[{self.c['cyan'][1]}m{string}\033[0m"

        def white_bg(self, string: str) -> str:
            return f"\033[{self.c['white'][1]}m{string}\033[0m"

        def bright_black_bg(self, string: str) -> str:
            return f"\033[{self.c['bright_black'][1]}m{string}\033[0m"

        def bright_red_bg(self, string: str) -> str:
            return f"\033[{self.c['bright_red'][1]}m{string}\033[0m"

        def bright_green_bg(self, string: str) -> str:
            return f"\033[{self.c['bright_green'][1]}m{string}\033[0m"

        def bright_yellow_bg(self, string: str) -> str:
            return f"\033[{self.c['bright_yellow'][1]}m{string}\033[0m"

        def bright_blue_bg(self, string: str) -> str:
            return f"\033[{self.c['bright_blue'][1]}m{string}\033[0m"

        def bright_magenta_bg(self, string: str) -> str:
            return f"\033[{self.c['bright_magenta'][1]}m{string}\033[0m"

        def bright_cyan_bg(self, string: str) -> str:
            return f"\033[{self.c['bright_cyan'][1]}m{string}\033[0m"

        def bright_white_bg(self, string: str) -> str:
            return f"\033[{self.c['bright_white'][1]}m{string}\033[0m"


if __name__ == '__main__':
    print('Do not run this file directly.')
