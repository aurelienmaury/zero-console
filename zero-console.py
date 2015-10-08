#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cmd2 import Cmd
import zmq
import argparse


def main():
    cli = ZeroConsole()
    cli.prompt = '| zero-console > '
    cli.cmdloop()


class ZeroConsole(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.cli_parser = argparse.ArgumentParser()

        subparsers = self.cli_parser.add_subparsers(help='internal commands')

        publish_parser = subparsers.add_parser('publish', help='publish')
        publish_parser.add_argument('--to', dest="to", metavar='PATH', type=str,
                                    help='acoustic model directory', required=True)

    def do_publish(self, line):
        subcmd = 'publish ' + line
        args = self.cli_parser.parse_args(args=subcmd.split())
        self.publish_target = args.to
        self.zmq_ctx = zmq.Context()
        self.sock = self.zmq_ctx.socket(zmq.PUB)
        self.sock.bind(self.publish_target)
        print "Now publishing to: " + self.publish_target

    def do_pub(self, line):
        self.sock.send(line)
        print 'Sent: ' + self.publish_target + ' ==> ' + line

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    main()
