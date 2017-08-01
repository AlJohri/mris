#!/usr/bin/env python3

import sys
import json
import textwrap
import logging
import argparse
import itertools

from mris.search import search

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        """
        don't show error message if you just type "mris"
        """
        messages_to_mute = [
            "the following arguments are required: %s" % word for word in ('command',)
        ]
        if message not in messages_to_mute:
            sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def cli():
    global_description = """
    examples:
    mris search ...
    """
    global_description = textwrap.dedent(global_description)
    formatter_class = lambda prog: argparse.RawDescriptionHelpFormatter(prog, max_help_position=32)

    parser = CustomArgumentParser(
        prog='mris',
        description=global_description,
        formatter_class=formatter_class)
    subparsers = parser.add_subparsers(dest='command', parser_class=CustomArgumentParser)
    subparsers.required = True

    shared_parser = argparse.ArgumentParser(add_help=False)
    shared_parser.add_argument('--verbose', default=False, action='store_true')

    def create_search_parser(parent_subparsers, shared_parsers=[]):

        def cli_search(args):
            for listing in itertools.islice(search(), args.limit):
                print(json.dumps(listing))

        parser = parent_subparsers.add_parser(
            'search',
            description=global_description,
            formatter_class=formatter_class,
            help='search',
            parents=shared_parsers)

        parser.add_argument('--limit', type=int)
        parser.set_defaults(func=cli_search)

    create_search_parser(subparsers, shared_parsers=[shared_parser])

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format=
            "[%(name)s | Thread: %(thread)d %(threadName)s | "
            "Process: %(process)d %(processName)s] %(asctime)s %(message)s")
        logging.getLogger('requests').setLevel(logging.WARNING)
        logging.getLogger('urllib3').setLevel(logging.WARNING)

    return args

def main():
    args = cli()
    args.func(args)

if __name__ == '__main__':
    main()
