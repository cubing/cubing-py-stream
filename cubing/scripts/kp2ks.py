import sys
import argparse
import yaml
from cubing.kpuzzle.puzdef import PuzDef


def process(file):
    with open(file) as reader:
        d = yaml.safe_load(reader)
        puzdef = PuzDef.from_dict(d)
    print(puzdef.to_ksolve())


def add_arguments(parser):
    parser.add_argument("file")
    return parser


def main():
    parser = add_arguments(argparse.ArgumentParser())
    options = vars(parser.parse_args(sys.argv[1:]))
    process(**options)


if __name__ == '__main__':
    main()
