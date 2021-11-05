import sys
import os.path
import yaml

KPATTERN_FILENAME = "../puzzles/3x3x3-speffz.kpattern.yaml"
with open(os.path.join(
        os.path.dirname(__file__),
        KPATTERN_FILENAME)) as reader:
    KPATTERN = yaml.safe_load(reader)


def is_ll(cls, t):
    s = cls.new()
    p = cls.from_dict(KPATTERN['patterns']['LL'])
    return t.match_old(s, p)


def is_f2l(cls, t):
    s = cls.new()
    p = cls.from_dict(KPATTERN['patterns']['F2L'])
    return t.match(s, p)


def is_cmll(cls, t):
    s = cls.new()
    p = cls.from_dict(KPATTERN['patterns']['CMLL'])
    return t.match(s, p)


def is_cross(cls, t):
    s = cls.new()
    p = cls.from_dict(KPATTERN['patterns']['CROSS'])
    return t.match(s, p)

def from_alg2(cls, steps):
    if steps.startswith('[') and \
       steps.endswith(']'):
        steps = steps.lstrip('[')
        steps = steps.rstrip(']')
        # print(repr(steps))
        if ',' in steps:
            a, b = steps.split(',')
            # print(repr(a), repr(b))
            return cls.from_alg(a).alg(b)(cls.from_alg(b).alg(a).__neg__())
    return None

if __name__ == '__main__':
    # from birdf2l import unhand
    from cubing.x3_speffz import Transform as X3SP
    for line in sys.stdin.readlines():
        line = line.strip()
        try:
            line = line.strip()
            parts = line.split(' ')
            if parts[0].startswith('U'):
                parts = parts[1:]
            if parts[-1].startswith('U'):
                parts = parts[:-2]
            line = ' '.join(parts)
            # line = unhand.optimize(line)
            # print(line)
            t = X3SP.from_alg(line)
            # t = from_alg2(X3SP, line)
            #if t is None:
            #    continue
            if is_ll(X3SP, t):
                print(line)
            # if is_cmll(X3SP, t) and not is_ll(X3SP, t):
            #     print(line)
            # t = t.rotate("y2")
            # if is_ll(X3SP, t):
            # if is_cmll(X3SP, t) and not is_ll(X3SP, t):
            #     print(line, "y2")
        except Exception as exc:
            print(repr(exc))
