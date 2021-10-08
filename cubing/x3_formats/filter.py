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
    return t.match(s, p)


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


if __name__ == '__main__':
    # from birdf2l import unhand
    from birdpuz.x3_speffz import Transform as T
    for line in sys.stdin.readlines():
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
            t = T.from_alg(line)
            # print(repr(t))
            # if is_ll(T, t):
            if is_cmll(T, t) and not is_ll(T, t):
                print(line)
            t = t.rotate("y2")
            # if is_ll(T, t):
            if is_cmll(T, t) and not is_ll(T, t):
                print(line, "y2")
        except Exception as exc:
            print(repr(exc))
