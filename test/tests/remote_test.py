#!/usr/bin/env python

from os import path
import argparse
import project_root
from helpers.helpers import call


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('remote', metavar='HOSTADDR:PANTHEON-DIR')
    args = parser.parse_args()
    remote = args.remote

    test_py = path.join(project_root.DIR, 'test', 'test.py')

    # test a receiver-first scheme
    cc = 'default_tcp'

    cmd = ['python', test_py, 'remote', remote, '-t', '5', '--schemes', cc]
    assert call(cmd) == 0

    cmd = ['python', test_py, 'remote', remote, '-t', '5',
           '--run-times', '2', '--schemes', cc]
    assert call(cmd) == 0

    cmd = ['python', test_py, 'remote', remote, '-t', '5',
           '--sender', 'remote', '--schemes', cc]
    assert call(cmd) == 0

    cmd = ['python', test_py, 'remote', remote, '-t', '5', '-f', '2',
           '--interval', '2', '--schemes', cc]
    assert call(cmd) == 0

    # test a sender-first scheme
    cc = 'verus'

    cmd = ['python', test_py, 'remote', remote, '-t', '5', '--schemes', cc]
    assert call(cmd) == 0

    cmd = ['python', test_py, 'remote', remote, '-t', '5',
           '--sender', 'remote', '--schemes', cc]
    assert call(cmd) == 0


if __name__ == '__main__':
    main()