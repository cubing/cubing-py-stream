import numpy


def positions(ls, e):
    for k, v in enumerate(ls):
        if v == e:
            yield k

def summod(n, m):
    return sum(map(int, numpy.base_repr(n, m))) % m

# EO requires:
# 4095 for 3x3x3-full-cube
#   15 for 3x3x3-last-layer
#
# A001969(2048) = 4095
# A001969(4095) = 8189
# CACHE2 = [sum(map(int, numpy.base_repr(i, 2))) % 2
#           for i in range(8200)]
# CACHE2Z = list(positions(CACHE2, 0))


# CO requires:
# 6560 for 3x3x3-full-cube
#   40 for 3x3x3-last-layer
#
# A079498(2187) = 6559
# A079498(3280) = 9839
# A079498(6560) = 19677
# CACHE3 = [sum(map(int, numpy.base_repr(i, 3))) % 3
#           for i in range(20000)]
# CACHE3Z = list(positions(CACHE3, 0))


# This doesn't work
# A079498(1) = 7
# A079498(2) = 10
# () = 4096
# CACHE4 = [sum(map(int, numpy.base_repr(i, 4))) % 4
#           for i in range(20000)]
# CACHE4Z = list(positions(CACHE4, 0))



def A001969(n):
    n -= 1
    return n*2 + (2 - summod(n, 2))


def A079498(n):
    n -= 1
    return n*3 + (3 - summod(n, 3))


def A001969i(n):
    # if n > CACHE2Z[-1]:
    #     raise ValueError("{} > {}".format(n, CACHE2Z[-1]))
    # try:
    #     return CACHE2Z.index(n) + 1
    # except Exception:
    #     return -1
    return int(n/2) + 1


def A079498i(n):
    # if n > CACHE3Z[-1]:
    #     raise ValueError("{} > {}".format(n, CACHE3Z[-1]))
    # try:
    #     return CACHE3Z.index(n) + 1
    # except Exception:
    #     return -1
    return int(n/3) + 1
    
