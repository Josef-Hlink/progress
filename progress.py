#!/usr/bin/env python3
"""
main script for a python progress bar
---
Initial commit: 01-04-2022
Author: J.D. Hamelink
"""

from style import Style

class ProgressBar:
    def __init__(self, n_iterations: int, bar_width: int = 50, char: str = '=', head: str = '>', todo: str = '-', braces: str = '[]',
                 spinner: bool = True, percentage: bool = True, color: str = None, bg_color: str = None, preset: str = None) -> None:
        """
        Progress bar for visualizing a process with fixed number of iterations
        ---
        params:
            - n_iterations: [int] total number of iterations to be processed
            - bar_width: [int] width of progress bar in characters
            - char: [str] *single* character representing the loaded portion of the bar
            - head: [str] *single* character leading the loaded portion of the bar
            - todo: [str] *single* character representing the portion of the bar that still has to be loaded
            - braces: [str] *two* characters that encapsulate the bar
            - spinner: [bool] set to True for a spinner in the suffix
            - percentage: [bool] set to True for a percentage in the suffix
            - color: [str] color to set all three bar characters as
            - bg_color: [str] color to set the backgrounds for all three bar characters as
            - preset: [str] choose from a select few presets {minimal, oldschool}
        """
        self.n_iters = n_iterations
        self.bar_width = bar_width
        
        self.show_spinner = spinner
        self.show_percentage = percentage

        self._config()
        self.set_char(char, color, bg_color)
        self.set_head(head, color, bg_color)
        self.set_todo(todo, color, bg_color)
        self.set_braces(braces, color, bg_color)
        self.set_preset(preset)

        self.i = 0
        self.done = False
        pass

    def __call__(self) -> None:
        """Wrapper for update function"""
        return self._update()

    def _config(self) -> None:
        """Set configurations: spinner frames and style object"""
        self.spinner_frames = ['/', '-', '\\', '|'] if self.show_spinner else ['', '', '', '']
        self.S = Style()
        pass

    def set_preset(self, preset: str) -> None:
        """
        Choose a predefined style configuration
        ---
        currently supported:
            - minimal
            - oldschool
        """
        if preset == 'minimal':
            self.spinner_frames = ['', '', '', '']
            self.show_percentage = False
            self.set_braces('[]', color = 'blue', bg_color = 'white')
            self.set_char('━', color = 'blue', bg_color = 'white')
            self.style('bold', 'base')
            self.set_head('►', color = 'blue', bg_color = 'white')
            # self.style()
            self.set_todo('━', color = 'blue', bg_color = 'white')
            self.style('faint', 'todo')
        elif preset == 'oldschool':
            self.spinner_frames = ['', '', '', '']
            self.show_percentage = False
            self.set_braces('  ', color = 'green', bg_color = 'black')
            self.set_char('■', color = 'green', bg_color = 'black')
            self.set_head('■', color = 'green', bg_color = 'black')
            self.set_todo('□', color = 'green', bg_color = 'black')
            self.style('faint', 'todo')

    def set_char(self, char: str = None, color: str = None, bg_color: str = None) -> None:
        """Set *single* character to represent the loaded portion of the progress bar"""
        if char is None:
            char = self.base_char                       # take the character that is already set
        elif not self._check_char(char):
            raise ValueError(f'Invalid base character {char} with length {len(char)}, choose a single character')
        if color is not None:
            char = self.S.set_color(color, char)        # add foreground color to character
        if bg_color is not None:
            char = self.S.set_bg_color(bg_color, char)  # add background color to character
        self.base_char = char                           # store as attribute

    def set_head(self, char: str = None, color: str = None, bg_color: str = None) -> None:
        """Set *single* character to represent the head of the loaded portion of the progress bar"""
        if char is None:
            char = self.head_char                       # take the character that is already set
        elif not self._check_char(char):
            raise ValueError(f'Invalid head character {char} with length {len(char)}, choose a single character')
        if color is not None:
            char = self.S.set_color(color, char)        # add foreground color to character
        if bg_color is not None:
            char = self.S.set_bg_color(bg_color, char)  # add background color to character
        self.head_char = char                           # store as attribute
    
    def set_todo(self, char: str = None, color: str = None, bg_color: str = None) -> None:
        """Set *single* character to represent the portion of the progress bar that has yet to be loaded"""
        if char is None:
            char = self.todo_char                       # take the character that is already set
        elif not self._check_char(char):
            raise ValueError(f'Invalid todo character "{char}" with length {len(char)}, choose a single character')
        if color is not None:
            char = self.S.set_color(color, char)        # add foreground color to character
        if bg_color is not None:
            char = self.S.set_bg_color(bg_color, char)  # add background color to character
        self.todo_char = char                           # store as attribute
    
    def set_braces(self, chars: str = None, color: str = None, bg_color: str = None) -> None:
        """Set *two* characters as braces for the bar"""
        if chars is None:
            open_brace = self.open_brace_char                           # take the characters that are already set
            close_brace = self.close_brace_char                         # ""
        else:
            if not self._check_braces(chars):
                raise ValueError(f'Invalid brace characters "{chars}" with length {len(chars)}, choose exactly two characters')
            open_brace = chars[0]                                       # split valid brace set into two characters
            close_brace = chars[1]                                      # ""
        if color is not None:
            open_brace = self.S.set_color(color, open_brace)            # add foreground color to characters
            close_brace = self.S.set_color(color, close_brace)          # ""
        if bg_color is not None:
            open_brace = self.S.set_bg_color(bg_color, open_brace)      # add background color to characters
            close_brace = self.S.set_bg_color(bg_color, close_brace)    # ""
        self.open_brace_char = open_brace                               # store as attributes
        self.close_brace_char = close_brace                             # ""

    def style(self, effect: str, part: str = None) -> None:
        """
        Add a style to a part of the bar
        ---
        params:
            - effect: [str] effect to be applied to a character, currently supported:
                * bold, faint, italic, underline, blink
            - part: [str] part of the bar to be styled, currently supported:
                * base, head, todo
        ---
        TODO add support for multiple effects and multiple parts
        """
        if effect not in ['bold', 'faint', 'italic', 'underline', 'blink']:
            raise ValueError(f'Invalid effect "{effect}", only bold, faint, italic, underline and blink are supported')
        apply_effect: function = getattr(Style, effect)                 # retrieve effect method from Style based on given string
        if part not in ['base', 'head', 'todo']:                        # TODO add support for braces, and suffix parts
            raise ValueError(f'Invalid part "{part}", only base, head and todo are supported')
        char_before = getattr(self, part+'_char')                       # retrieve bar attribute to be styled
        setattr(self, part+'_char', apply_effect(Style(), char_before)) # store the new value in this attribute

    def _update(self) -> None:
        """Update the progress bar by one iteration"""
        self.i += 1
        if self.i == self.n_iters:
            self.done = True
        
        steps = int(self.bar_width * (self.i) // self.n_iters)      # number of blocks that the bar should be filled with
        percentage = round(100 * (self.i) / float(self.n_iters))    # calculate percentage for suffix
        
        line = self._compose(steps, percentage)
        self._render(line)

    def _check_char(self, char: str) -> bool:
        """Check if a given character is usable in the progress bar"""
        return isinstance(char, str) and len(self.S.get_original(char)) == 1
    
    def _check_braces(self, chars: str) -> bool:
        """Check if a given set of characters is usable as a set of braces for the progress bar"""
        return isinstance(chars, str) and len(chars) == 2

    def _compose(self, steps: int, percentage: int) -> str:
        """Compose the complete line that is to be printed"""
        spin_char = self.spinner_frames[self.i%4]
        bar = ( (steps * self.base_char) +                  # loaded portion
                self.head_char +                            # head
                (self.bar_width-steps) * self.todo_char)    # todo portion
        suffix = f'{spin_char} {percentage}%' if self.show_percentage else spin_char
        return self.open_brace_char + bar + self.close_brace_char + suffix
    
    def _render(self, line: str) -> None:
        """Print the line on by replacing the previous line"""
        if self.done:   # if process is finished, suffix is changed and line gets a newline character
            line = f'{self.open_brace_char}{(self.bar_width+1)*self.base_char}{self.close_brace_char} complete\n'
        print(f'\r{line}', end='')


if __name__ == '__main__':
    print('Do not run this file directly.')
