#!/usr/bin/env python3
"""
main script for a python progress bar
---
Initial commit: 01-04-2022
Author: J.D. Hamelink
"""

class ProgressBar:
    def __init__(self, n_iterations: int, bar_width: int = 50, char: str = '-', head: str = '>', todo: str = ' ',
                 spinner: bool = True, percentage: bool = True) -> None:
        """
        Progress bar for visualizing a process with fixed number of iterations
        ---
        params:
            - n_iterations: [int] total number of iterations to be processed
            - bar_width:    [int] width of progress bar in characters
            - char:         [str] *single* character representing the loaded portion of the bar
            - head:         [str] *single* character leading the loaded portion of the bar
            - todo:         [str] *single* character representing the portion of the bar that still has to be loaded
            - spinner:      [bool] set to True for a spinner in the suffix
            - percentage:   [bool] set to True for a percentage in the suffix
        """
        self.n_iters = n_iterations
        self.bar_width = bar_width
        self.base_char = char
        self.head_char = head
        self.todo_char = todo
        self.show_spinner = spinner
        self.show_percentage = percentage

        self._config()
        self.iteration = 0
        self.done = False
        pass

    def __call__(self) -> None:
        """Wrapper for update function"""
        return self._update()

    def _update(self) -> None:
        """Update the progress bar by one iteration"""
        self.iteration += 1
        if self.iteration == self.n_iters:
            self.done = True
        
        steps = int(self.bar_width * (self.iteration) // self.n_iters)
        percentage = round(100 * (self.iteration) / float(self.n_iters))
        
        line = self._compose(steps, percentage)
        self._render(line)
        return
    
    def _config(self) -> None:
        """Set configurations, for now only spinner frames"""
        self.spinner_frames = ['/', '-', '\\', '|'] if self.show_spinner else ['', '', '', '']
        return

    def _compose(self, steps: int, percentage: int) -> str:
        """Compose the complete line that is to be printed"""
        spin_char = self.spinner_frames[self.iteration%4]
        bar = f'{steps*self.base_char}{self.head_char}{(self.bar_width-steps)*self.todo_char}'
        suffix = f'{spin_char} {percentage}%'
        return f'[{bar}]{suffix}'
    
    def _render(self, line: str) -> None:
        """Print the line on by replacing the previous line"""
        print(f'\r{line}', end='')
        if self.done:
            print()
        return

if __name__ == '__main__':
    print('Do not run this file directly.')
