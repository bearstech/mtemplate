#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import sys

from jinja2 import Template

parser = argparse.ArgumentParser(description='µtemplate')
parser.add_argument('--template', dest='template', default=None)
parser.add_argument('--dest', dest='dest', default=None)

def main():

    args = parser.parse_args()

    if args.template is None:
        t = sys.stdin
    else:
        t = open(args.template, 'r')

    template = Template(t.read())
    if args.dest is None:
        print template.render(ENV=os.environ)
    else:
        with open(args.dest, 'w') as f:
            f.write(template.render(ENV=os.environ))

if __name__ == '__main__':
    main()
