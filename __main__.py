#!/usr/bin/env python3
import sys
import argparse

from Stopwatch import stopwatch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--precision', required=False,
                        default=4, help='Floating pt precision limit.')
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
    output = {
            'start': 'Stopwatch is now running...',
            'reset': 'Stopwatch timer has been reset...',
            'stop': 'Stopwatch is stopped...',
            'quit': 'Thank you, goodbye...',
            'total': 'Calculating total...',
            'status': 'Checking status...',
            }
    choices = '\n'.join([
            'Please choose from the available actions:',
            '\tstatus - Check if stopwatch is stopped or running.',
            '\tstart  - Start a stopped stopwatch.',
            '\tstop   - Stop a running stopwatch.',
            '\treset  - Reset a stopped stopwatch.',
            '\ttotal  - Show time when stopped.',
            '\tquit   - Quit program.\n',
            'What would you like to do? ',
            ])
    try:
        while True:
            choice = input(choices)
            if choice in ('start', 'stop', 'reset', 'quit'):
                actions[choice]()
                sys.stdout.write('\n\n\t>> %s\n' % output[choice])
            elif choice in ('total', 'status'):
                sys.stdout.write('\n\n\t>> %s\n' % output[choice])
                sys.stdout.write('\t>> %s is %s\n' % (choice, actions[choice]()))
            else:
                sys.stdout.write("\n\tI'm sorry, I didn't understand.\n")
            sys.stdout.write('\n')
    except KeyboardInterrupt:
        sys.stdout.write('\nGoodbye!\n')
        sys.exit()

if __name__ == '__main__':
    main()
