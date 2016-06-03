#!/usr/bin/env python3
#
# Charles Pantoga
# (C) 2016
#

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


# Interactive Stopwatch Program
if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--precision', required=False, default=None,
                        choices=range(17), help='Floating pt precision limit.')
    args = parser.parse_args()

    watch = Stopwatch(precision=args.precision)

    actions = {
            'status': watch.status,
            'start': watch.start,
            'reset': watch.reset,
            'total': watch.total,
            'stop': watch.stop,
            'quit': sys.exit,
            }
    action_output = {
            'start': 'Stopwatch is now running...',
            'reset': 'Stopwatch timer has been reset...',
            'stop': 'Stopwatch is stopped...',
            'quit': 'Thank you, goodbye...',
            }
    property_output = {
            'total': 'Calculating total...',
            'status': 'Checking status...',
            }

    def choices():
        return '''\
Please choose from the available actions:
    status - Check if stopwatch is stopped or running.
    start  - Start a stopped stopwatch.
    stop   - Stop a running stopwatch.
    reset  - Reset a stopped stopwatch.
    total  - Show time when stopped.
    quit   - Quit program.

What would you like to do? '''

    try:
        while True:
            choice = input(choices())
            if choice in action_output.keys():
                actions[choice]()
                print("\n\n\t>> " + action_output[choice])
            elif choice in property_output.keys():
                print("\n\n\t>> " + property_output[choice])
                print("\t>> {} is {}".format(choice, actions[choice]()))
            else:
                print("\n\tI'm sorry, I didn't understand.")
            print('\n')

    except KeyboardInterrupt:
        print()
        print("Goodbye!")
        sys.exit()
