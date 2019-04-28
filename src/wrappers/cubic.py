#!/usr/bin/env python

from subprocess import check_call

import arg_parser


def main():
    args = arg_parser.receiver_first()

    if args.option == 'deps':
        print 'iperf'
        return

    if args.option == 'receiver':
        cmd = ['iperf', '-Z', 'cubic', '-s', '-p', args.port]
        check_call(cmd)
        return

    if args.option == 'sender':
        cmd = ['iperf', '-Z', 'cubic', '-c', args.ip, '-p', args.port,
        # Changes for running beyond 7200 secs -- START
            #    '-t', '75']
               '-t', '10000']
        # Changes for running beyond 7200 secs -- END
        check_call(cmd)
        return


if __name__ == '__main__':
    main()
