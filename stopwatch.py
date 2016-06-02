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
    def __init__(self):
        self.__is_running = False
        self.__times = []

    def start(self):
        if self.__is_running:
            raise NotStoppedError
        self.__is_running = True
        timepair = {'start': time.time(),
                    'stop': None}
        self.__times.append(timepair)

    def stop(self):
        if not self.__is_running:
            raise NotRunningError
        timepair = self.__times[-1]
        timepair['stop'] = time.time()
        self.__is_running = False

    def reset(self):
        if self.__is_running:
            raise NotStoppedError
        self.__times = []

    def total(self):
        return sum(t['stop']-t['start'] for t in self.__times)

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
    parser.add_argument('-p', '--precision', required=False,
                        help='Number of decimal places displayed.')
    args = parser.parse_args()
    print(args.precision)

    print("Stopwatch Program\n====================\n\n")

    def choices():
        return '''\
    Please choose from the available actions:
        status - Check if stopwatch is stopped or running.
        start  - Start a stopped stopwatch.
        stop   - Stop a running stopwatch.
        reset  - Reset a stopped stopwatch.
        total  - Show time when stopped.
        quit   - Quit program.

    Action: '''

    watch = Stopwatch()

    actions = {
        'status': watch.status,
        'start': watch.start,
        'reset': watch.reset,
        'total': watch.total,
        'stop': watch.stop,
        'quit': sys.exit,
        }

    action_output = {
        'start': 'Stopwatch is now running...\n',
        'reset': 'Stopwatch timer has been reset...\n',
        'stop': 'Stopwatch is stopped...\n',
        'quit': 'Thank you, goodbye...\n',
        }

    property_output = {
        'total': 'Calculating total...',
        'status': 'Checking status...',
        }


    try:
        while True:
            choice = input(choices())
            if choice in action_output.keys():
                actions[choice]()
                print("\n\t>> " + action_output[choice] + "\n")
            elif choice in property_output.keys():
                print("\n\t>> " + property_output[choice])
                attribute = actions[choice]()

                if isinstance(attribute, float):
                    fmt = "\t>> {} if {:."+args.precision+"f}\n"
                else:
                    fmt = "\t>> {} is {}"

                print(fmt.format(choice, attribute))
            else:
                print("\n\tI'm sorry, I didn't understand.\n")
    except KeyboardInterrupt:
        print()
        print("Goodbye!")
        sys.exit(-1)
