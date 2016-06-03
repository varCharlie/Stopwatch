#!/usr/bin/env python3
#
# Charles Pantoga
# (C) 2016
#

import time

# Stopwatch Exception Classes
class StopwatchError(Exception):
    pass

class InvalidStateError(StopwatchError):
    pass

class NotRunningError(InvalidStateError):
    def __init__(self):
        msg = "Invalid State: Expected Stopwatch to be running."
        super().__init__(msg)

class NotStoppedError(InvalidStateError):
    def __init__(self, caller):
        msg = "Invalid State: Expected Stopwatch to be stopped."
        super().__init__(msg)


# Main Stopwatch Class
class Stopwatch:
    '''Stopwatch for keeping track of time'''
    def __init__(self, *, precision=None):
        self.__is_running = False
        self.__times = []
        self.__precision = precision

    def start(self):
        if self.__is_running:
            raise NotStoppedError
        self.__is_running = True
        self.__times.append({
            'start': time.time(),
            'stop': None,
            })

    def stop(self):
        if not self.__is_running:
            raise NotRunningError
        self.__times[-1]['stop'] = time.time()
        self.__is_running = False

    def reset(self):
        if self.__is_running:
            raise NotStoppedError
        self.__times = []

    def total(self):
        total = sum(t['stop']-t['start'] for t in self.__times)
        if self.__precision:
            return float(str('{:0' + str(self.__precision) + 'f}').format(total))
        else:
            return total

    def status(self):
        if self.__is_running:
            return "running"
        else:
            return "stopped"


# Interactive Stopwatch Program
if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--precision', required=False, default=None,
                        help='Number of decimal places displayed.')
    args = parser.parse_args()
    print(args.precision)

    print("Stopwatch Program\n====================\n\n")

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
        sys.exit(-1)
