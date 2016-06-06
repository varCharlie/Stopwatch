#!/usr/bin/env python3
'''Stopwatch Test Program'''
##
# Name: Charles Pantoga
# Gmail: suspects
# Github: varcharlie & varcharlez
# Copyright 2016 (C)
#
# The is just a simple program that uses the stopwatch class
# that I wrote to answer somebody's stackoverflow question.
##

import argparse
import sys

import stopwatch

def main():
    choices = ("Please choose from the available actions:\n"
               "    status - Check if stopwatch is stopped or running.\n"
               "    start  - Start a stopped stopwatch.\n"
               "    stop   - Stop a running stopwatch.\n"
               "    reset  - Reset a stopped stopwatch.\n"
               "    total  - Show time when stopped.\n"
               "    quit   - Quit program.\n\n"
               "  What would you like to do? ")

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--precision', required=False, default=None,
                        help='Floating pt precision limit.')
    args = parser.parse_args()

    watch = stopwatch.Stopwatch(precision=args.precision)

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


    try:
        while True:
            choice = input(choices)
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

if __name__ == '__main__':
    main()
