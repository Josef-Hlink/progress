#!/usr/bin/env python3
"""
main script for a python progress bar
---
Initial commit: 01-04-2022
Author: J.D. Hamelink
"""

from style import Style

class ProgressBar:
    def __init__(self, n_iterations: int, bar_width: int = 50, char: str = '=', head: str = '>', todo: str = '-',
                 spinner: bool = True, percentage: bool = True, color: str = None, bg_color: str = None) -> None:
        """
        Progress bar for visualizing a process with fixed number of iterations
        ---
        params:
            - n_iterations: [int] total number of iterations to be processed
            - bar_width: [int] width of progress bar in characters
            - char: [str] *single* character representing the loaded portion of the bar
            - head: [str] *single* character leading the loaded portion of the bar
            - todo: [str] *single* character representing the portion of the bar that still has to be loaded
            - spinner: [bool] set to True for a spinner in the suffix
            - percentage: [bool] set to True for a percentage in the suffix
            - color: [str] color to set all three bar characters as
            - bg_color: [str] color to set the backgrounds for all three bar characters as
        """
        self.n_iters = n_iterations
        self.bar_width = bar_width
        
        self.show_spinner = spinner
        self.show_percentage = percentage

        self._config()
        self.set_char(char, color, bg_color)
        self.set_head(head, color, bg_color)
        self.set_todo(todo, color, bg_color)

        self.i = 0
        self.done = False
        pass

    def __call__(self) -> None:
        """Wrapper for update function"""
        return self._update()

    def _config(self) -> None:
        """Set configurations: spinner frames and available colors"""
        self.spinner_frames = ['/', '-', '\\', '|'] if self.show_spinner else ['', '', '', '']
        self.available_colors = set(Style().c.keys())
        pass

    def set_char(self, char: str = None, color: str = None, bg_color: str = None) -> None:
        """Set *single* character to represent the loaded portion of the progress bar"""
        if char is None:
            char = self.base_char
        if not self._check_char(char):
            raise ValueError(f'Invalid character {char} with length {len(char)}, choose a single character')
        if color is not None:
            char = self._set_color(color, char)
        if bg_color is not None:
            char = self._set_bg_color(bg_color, char)
        self.base_char = char

    def set_head(self, char: str = None, color: str = None, bg_color: str = None) -> None:
        """Set *single* character to represent the head of the loaded portion of the progress bar"""
        if char is None:
            char = self.head_char
        if not self._check_char(char):
            raise ValueError(f'Invalid character {char} with length {len(char)}, choose a single character')
        if color is not None:
            char = self._set_color(color, char)
        if bg_color is not None:
            char = self._set_bg_color(bg_color, char)
        self.head_char = char
    
    def set_todo(self, char: str = None, color: str = None, bg_color: str = None) -> None:
        """Set *single* character to represent the portion of the progress bar that has yet to be loaded"""
        if char is None:
            char = self.todo_char
        if not self._check_char(char):
            raise ValueError(f'Invalid character "{char}" with length {len(char)}, choose a single character')
        if color is not None:
            char = self._set_color(color, char)
        if bg_color is not None:
            char = self._set_bg_color(bg_color, char)
        self.todo_char = char
    
    def _set_color(self, color: str, char: str = None) -> str:
        """Set the color of a character (base, head, or todo)"""
        if color not in self.available_colors:
            raise ValueError(f'Invalid color "{color}", look at the README to see all available colors') # TODO actually write README
        return getattr(Style, color)(Style(), char)
    
    def _set_bg_color(self, color: str, char: str = None):
        """Set the background color of a character (base, head, or todo)"""
        bg_color = color+'_bg'
        if color not in self.available_colors:
            raise ValueError(f'Invalid background color "{color}", look at the README to see all available colors') # TODO actually write README
        return getattr(Style, bg_color)(Style(), char)

    def _update(self) -> None:
        """Update the progress bar by one iteration"""
        self.i += 1
        if self.i == self.n_iters:
            self.done = True
        
        steps = int(self.bar_width * (self.i) // self.n_iters)
        percentage = round(100 * (self.i) / float(self.n_iters))
        
        line = self._compose(steps, percentage)
        self._render(line)

    def _check_char(self, char: str) -> bool:
        """Check if a given character is useable in the progress bar"""
        return isinstance(char, str) and len(char) == 1

    def _compose(self, steps: int, percentage: int) -> str:
        """Compose the complete line that is to be printed"""
        spin_char = self.spinner_frames[self.i%4]
        bar = f'{steps*self.base_char}{self.head_char}{(self.bar_width-steps)*self.todo_char}'
        suffix = f'{spin_char} {percentage}%' if self.show_percentage else spin_char
        return f'[{bar}]{suffix}'
    
    def _render(self, line: str) -> None:
        """Print the line on by replacing the previous line"""
        if self.done:
            line = f'[{(self.bar_width+1)*self.base_char}] complete\n'
        print(f'\r{line}', end='')


if __name__ == '__main__':
    print('Do not run this file directly.')
