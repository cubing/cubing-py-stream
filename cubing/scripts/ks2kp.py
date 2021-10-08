import sys
import argparse
import json
from cubing.kpuzzle.puzdef import PuzDef
from cubing.ksolve.reflow import json_reflow


def process(file):
    with open(file) as reader:
        puzdef = PuzDef.from_reader(reader)
    print(json_reflow(json.dumps(puzdef.__getstate__(), indent=4)))


def add_arguments(parser):
    parser.add_argument("file")
    return parser


def main():
    parser = add_arguments(argparse.ArgumentParser())
    options = vars(parser.parse_args(sys.argv[1:]))
    process(**options)


if __name__ == '__main__':
    main()
