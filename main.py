#!/usr/bin/env python3
import sys
import argparse

import stopwatch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--precision', required=False, default=None,
                        help='Floating pt precision limit.')
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
    choices = '\n'.join([
            "Please choose from the available actions:"
            "\tstatus - Check if stopwatch is stopped or running."
            "\tstart  - Start a stopped stopwatch."
            "\tstop   - Stop a running stopwatch."
            "\treset  - Reset a stopped stopwatch."
            "\ttotal  - Show time when stopped."
            "\tquit   - Quit program.\n"
            "What would you like to do? "
            ])
    try:
        while True:
            choice = input(choices())
            if choice in ('start', 'stop', 'reset', 'quit'):
            elif choice in ('total', 'status'):
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
        print("\nGoodbye!")
        sys.exit()

if __name__ == '__main__':
    main()
