import os.path
import re
import six
import pandas
import argparse
from .alg import canonicalize


def format_annotation(is_header=False, **d):
    if is_header:
        print("canon_alg,input_alg")
    else:
        return "{alg},{input_alg}".format(**d)

def annotate(alg, notes=None):
    return {
        "alg": alg,
    }
    
def add_arguments(parser):
    parser.add_argument("--auf", action='store_true')
    return parser

def main():
    import sys
    parser = add_arguments(argparse.ArgumentParser())
    options = vars(parser.parse_args(sys.argv[1:]))
    isoob = options.get('auf', False)
    iscsv = True
    if iscsv:
        format_annotation(True)
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if line.startswith('htm'):
            continue
        if not line.strip():
            continue
        line = line.strip()
        parts = line.split(',')
        try:
            if len(parts) == 0:
                raise ValueError
            elif len(parts) == 1:

                # 1 column means: alg
                alg0 = parts[0]
                names = ''
            else:
                alg0 = None
                raise ValueError

            alg = canonicalize(alg0, oob=isoob)
            ann = annotate(alg)
            ann["input_alg"] = alg0
            if iscsv:
                print(format_annotation(**ann))
        except Exception as exc:
            print(repr(exc))
            raise

if __name__ == '__main__':
    main()
