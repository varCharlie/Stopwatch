#!/usr/bin/env python3
'''Stopwatch class for keeping track of time.'''
##
# Charles Pantoga, (C) 2016
# Gmail Account: suspects
#  
##

import time

class StopwatchError(Exception):
    '''Stopwatch Base Error Class'''
    pass

class InvalidStateError(StopwatchError):
    '''Invalid State Base Error Class'''
    pass

class NotRunningError(InvalidStateError):
    '''Stopwatch Is Not Running Error'''
    def __init__(self):
        msg = "Invalid State: Expected Stopwatch to be running."
        super().__init__(msg)

class NotStoppedError(InvalidStateError):
    '''Stopwatch Is Not Stopped Error'''
    def __init__(self, caller):
        msg = "Invalid State: Expected Stopwatch to be stopped."
        super().__init__(msg)


# Main Stopwatch Class
class Stopwatch:
    '''Stopwatch for keeping track of time'''
    def __init__(self, *, precision=None):
        self.__is_running = False
        self.__times = []
        if isinstance(precision, float):
            precision = str(precision).split('.')[0]
        if isinstance(precision, int):
            precision = str(precision)
        self.__precision = precision


    def start(self):
        '''Start the stopwatch if it's not already running'''
        if self.__is_running:
            raise NotStoppedError
        self.__is_running = True
        self.__times.append({
                'start': time.time(),
                'stop': None,
                })

    def stop(self):
        '''Stop the stopwatch if it's running'''
        if not self.__is_running:
            raise NotRunningError
        self.__times[-1]['stop'] = time.time()
        self.__is_running = False

    def reset(self):
        '''Reset the stopwatch if it's not running'''
        if self.__is_running:
            raise NotStoppedError
        self.__times = []

    def total(self):
        '''Calculate total time tracked if stopwatch is stopped'''
        if self.__is_running:
            raise NotStoppedError
        total = sum(t['stop']-t['start'] for t in self.__times)
        if self.__precision:
            return float(('{:.' + self.__precision + 'f}').format(total))
        else:
            return total

    def status(self, *, typename=str):
        output_map = {
                str: ('running', 'stopped'),
                bool: (True, False),
                int: (1, 0),
                }
        if self.__is_running:
            return output_map[typename][0]
        else:
            return output_map[typename][1]

