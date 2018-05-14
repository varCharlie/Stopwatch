#!/usr/bin/env python3
'''Stopwatch class for keeping track of time.'''
##
# Charles Pantoga, (C) 2016
# Gmail Account: suspects
#
##

import time

# Exception Wrappers
class StopwatchError(RuntimeError):
    '''Stopwatch base error class. Allows `except Exception:`'''
    @abstractmethod
    def __init__(self): pass

class NotRunningError(StopwatchError):
    '''Stopwatch Is Not Running Error'''
    def __init__(self):
        msg = "Invalid State: Expected Stopwatch to be running."
        super().__init__(msg)

class NotStoppedError(StopwatchError):
    '''Stopwatch Is Not Stopped Error'''
    def __init__(self):
        msg = "Invalid State: Expected Stopwatch to be stopped."
        super().__init__(msg)


# Main Stopwatch Class
class Stopwatch:
    '''Stopwatch for keeping track of time'''
    def __init__(self, *, precision=4):
        '''Instantiates a Stopwatch object
        Arguments:
            :precision - Determines how many 'decimal places'
                        will be included in the output.
        '''

        self.__is_running = False
        self.__times = []
        if isinstance(precision, float):
            self.__precision = str(precision).split('.')[0]
        else:
            self.__precision = str(precision)


    def start(self):
        '''Start the stopwatch if it's not already running
        Raises NotStoppedError if the stopwatch isn't running
        '''
        if self.__is_running:
            raise NotStoppedError
        self.__is_running = True
        self.__times.append({'start': time.time(), 'stop': None})

    def stop(self):
        '''Stop the stopwatch if it's running
        Raises NotRunningError if the stopwwatch is not running
        '''
        if not self.__is_running:
            raise NotRunningError
        self.__times[-1]['stop'] = time.time()
        self.__is_running = False

    def reset(self):
        '''Reset the stopwatch if it's not running
        Raises NotStoppedError if the stopwatch is still running
        '''
        if self.__is_running:
            raise NotStoppedError
        self.__times = []

    def total(self):
        '''Calculate total time tracked if stopwatch is stopped
        The precision attribute determines how many places after
        the decimal point should be present.
        '''
        if self.__is_running:
            raise NotStoppedError
        total = sum(t['stop']-t['start'] for t in self.__times)
        if self.__precision:
            return float(('{:.' self.__precision + 'f}').format(total))
        else:
            return total

    def status(self, *, typename=str):
        '''Used to determine whether the stopwatch is currently
        running. Takes an option keyword argument.
            :typename - Receive status as a specific type.
                        Must be str, bool, or int
        '''
        output_map = {
                str: ('running', 'stopped'),
                bool: (True, False),
                int: (1, 0),
                }
        if not isinstance(typename, output_map.keys()):
            raise ArgumentError("`typename` must be in the set {str, bool, int}")
        if self.__is_running:
            return output_map[typename][0]
        else:
            return output_map[typename][1]

