#!/usr/bin/env python

import os
from os import path
from subprocess import check_call

import arg_parser
import context
from helpers import utils


def main():
    args = arg_parser.receiver_first()

    cc_repo = path.join(context.third_party_dir, 'fillp-sheep')
    send_dir = path.join(cc_repo, 'client')
    recv_dir = path.join(cc_repo, 'server')
    send_src = path.join(send_dir, 'client')
    recv_src = path.join(recv_dir, 'server')

    if args.option == 'receiver':
        os.environ['LD_LIBRARY_PATH'] = recv_dir
        # Changes for running beyond 7200 secs -- START
        # cmd = [recv_src, '-s', '0.0.0.0', '-p', args.port, '-r', 'testcase001', '-t', '60']
        cmd = [recv_src, '-s', '0.0.0.0', '-p', args.port, '-r', 'testcase001', '-t', '10000']
        # Changes for running beyond 7200 secs -- END
        check_call(cmd, cwd=utils.tmp_dir)
        return

    if args.option == 'sender':
        os.environ['LD_LIBRARY_PATH'] = send_dir
        # Changes for running beyond 7200 secs -- START
        # cmd = [send_src, '-c', args.ip, '-p', args.port, '-r', 'testcase001', '-t', '60']
        cmd = [send_src, '-c', args.ip, '-p', args.port, '-r', 'testcase001', '-t', '10000']
        # Changes for running beyond 7200 secs -- END
        check_call(cmd, cwd=utils.tmp_dir)
        return


if __name__ == '__main__':
    main()
