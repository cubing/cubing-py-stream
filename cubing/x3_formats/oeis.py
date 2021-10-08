import numpy

CACHE2 = [sum(map(int, numpy.base_repr(i, 2))) % 2 for i in range(5000)]
CACHE3 = [sum(map(int, numpy.base_repr(i, 3))) % 3 for i in range(2000)]


def positions(ls, e):
    for k, v in enumerate(ls):
        if v == e:
            yield k


def A001969(n):
    return list(positions(CACHE2, 0))[n - 1]


def A079498(n):
    return list(positions(CACHE3, 0))[n - 1]


def A001969i(n):
    try:
        return list(positions(CACHE2, 0)).index(n) + 1
    except Exception:
        return -1


def A079498i(n):
    try:
        return list(positions(CACHE3, 0)).index(n) + 1
    except Exception:
        return -1
