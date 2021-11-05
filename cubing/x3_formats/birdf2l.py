"""
Variations of BirdF2L Speffz System:

- Last Layer (LL), e.g.: AaBbCcDd
- First 2 Layers (F2L), e.g.: AaBbCcDd/Vj
- Advanced First 2 Layers (AF2L), e.g.: AaBbCcDd/UfVjWnXr
- Whole Cube, e.g.: AaBbCcDd/UfVjWnXr/uvwx
- Image Cube, e.g.: AaBbCcDd/UfVjWnXr/uvwx/ULFRBD
- Truncated (LL + Image), e.g.: AaBbCcDd///ULFRBD

"""

MASK_C = "1 1 1 1  1 1 1 1             "
MASK_E = " 1 1 1 1  1 1 1 1 1111       "
MASK_M = "                       111111"
SOLVED_CODE = "AaBbCcDd/UfVjWnXr/uvwx/ULFRBD"
SOLVED_F2L = "AaBbCcDd/Vj"
SOLVED_LL = "AaBbCcDd"
SOLVED_MP = "ULFRBD"
SOLVED_MID = "UfVjWnXr/uvwx"

STOPS = [8, 17, 22]

EDGES_DATA = [
    ["a", "b", "c", "d", "f", "j",
     "n", "r", "u", "v", "w", "x"],
    ["q", "m", "i", "e", "l", "p",
     "t", "h", "k", "o", "s", "g"],
]

CORNERS_DATA = [
    ["A", "B", "C", "D", "U", "V", "W", "X"],
    ["R", "N", "J", "F", "L", "P", "T", "H"],
    ["E", "Q", "M", "I", "G", "K", "O", "S"],
]

# unused: "C", "O"
CENTERS_DATA = [
    # NOT Speffz related, perhaps build consensus?
    ["U", "L", "F", "R", "B", "D"],
    ["V", "K", "G", "S", "Y", "P"],
    ["W", "J", "H", "T", "Z", "M"],
    ["X", "I", "E", "Q", "A", "N"],
]


def _decode_po(data, ch):
    for io, _ in enumerate(data):
        for ip, ch2 in enumerate(data[io]):
            if ch == ch2:
                return ip, io
    return -1, -1


def decode(cls, prid):
    ep, eo = [], []
    cp, co = [], []
    mp, mo = [], []

    if len(prid) == len(SOLVED_F2L):
        prid = ''.join([
            prid[:len(SOLVED_LL)], "/",
            SOLVED_CODE[9:11], prid[9:11],
            SOLVED_CODE[13:]])
    if "///" in prid:
        prid = prid.replace("///", "/" + SOLVED_MID + "/")
    for stop in STOPS:
        if len(prid) < len(SOLVED_CODE):
            prid += SOLVED_CODE[len(prid):]
    # print("d", prid)

    for ix, ch in enumerate(list(prid)):
        if MASK_E[ix] == '1':
            p, o = _decode_po(EDGES_DATA, ch)
            ep.append(p)
            eo.append(o)
        if MASK_C[ix] == '1':
            p, o = _decode_po(CORNERS_DATA, ch)
            cp.append(p)
            co.append(o)
        if MASK_M[ix] == '1':
            p, o = _decode_po(CENTERS_DATA, ch)
            mp.append(p)
            mo.append(o)

    return cls.from_dict({
        "EDGES": {
            "permutation": ep,
            "orientation": eo,
        },
        "CORNERS": {
            "permutation": cp,
            "orientation": co,
        },
        "CENTERS": {
            "permutation": mp,
            "orientation": mo,
        },
    })


def _encode_po(data, p, o):
    return ord(data[o][p])


def encode(cls, pos):
    if not isinstance(pos, cls):
        raise TypeError("input must be a {} object".format(cls.__name__))

    ep = list(reversed(pos.EDGES.permutation))
    eo = list(reversed(pos.EDGES.orientation))
    cp = list(reversed(pos.CORNERS.permutation))
    co = list(reversed(pos.CORNERS.orientation))
    mp = list(reversed(pos.CENTERS.permutation))
    mo = list(reversed(pos.CENTERS.orientation))

    prid = bytearray(SOLVED_CODE.encode('latin1'))
    for ix, ch in enumerate(list(prid)):
        if MASK_E[ix] == '1':
            p, o = ep.pop(), eo.pop()
            prid[ix] = _encode_po(EDGES_DATA, p, o)
        if MASK_C[ix] == '1':
            p, o = cp.pop(), co.pop()
            prid[ix] = _encode_po(CORNERS_DATA, p, o)
        if MASK_M[ix] == '1':
            p, o = mp.pop(), mo.pop()
            prid[ix] = _encode_po(CENTERS_DATA, p, o)

    prid = prid.decode('latin1')
    for stop in STOPS:
        # print(prid)
        # print(SOLVED_CODE[stop:])
        # print("=", prid[:-len(SOLVED_CODE[stop:])])
        if prid.endswith(SOLVED_CODE[stop:]):
            prid = prid[:-len(SOLVED_CODE[stop:])]
    if prid.endswith(SOLVED_CODE[17:]) and \
       prid[9:11] == SOLVED_CODE[9:11] and \
       prid[13:17] == SOLVED_CODE[13:17]:
        prid = prid[:9] + prid[11:13]
    if SOLVED_MID in prid:
        prid = prid.replace(SOLVED_MID, "/")

    return prid


def orid_from_prid(birdf2l_prid):  # AaBbCcDd -> AaBbCcDd
    # TODO assert is_ll
    orid = ''.join(sorted(list(
        birdf2l_prid[0:8])))
    orid = ''.join([
        orid[0], orid[4],
        orid[1], orid[5],
        orid[2], orid[6],
        orid[3], orid[7]])
    return orid
