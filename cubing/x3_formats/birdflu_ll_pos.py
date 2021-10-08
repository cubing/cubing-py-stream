"""
Variations of Birdflu System:

- Last Layer Position Name (ll_pos),  e.g.: "Ao4A"
- Last Layer Position Code (ll_code), e.g.: "a1a1a1a1"

"""

EP_DATA = [
    ("A", (0, 1, 2, 3)),
    ("B", (2, 3, 0, 1)),
    ("C", (3, 2, 1, 0)),
    ("D", (1, 0, 3, 2)),
    ("E", (0, 2, 3, 1)),
    ("F", (0, 3, 1, 2)),
    ("G", (2, 1, 3, 0)),
    ("H", (3, 1, 0, 2)),
    ("I", (1, 3, 2, 0)),
    ("J", (3, 0, 2, 1)),
    ("K", (1, 2, 0, 3)),
    ("L", (2, 0, 1, 3)),
    ("a", (3, 0, 1, 2)),
    ("b", (1, 2, 3, 0)),
    ("c", (0, 3, 2, 1)),
    ("d", (2, 1, 0, 3)),
    ("e", (1, 0, 2, 3)),
    ("f", (2, 0, 3, 1)),
    ("g", (0, 2, 1, 3)),
    ("h", (2, 3, 1, 0)),
    ("i", (0, 1, 3, 2)),
    ("j", (1, 3, 0, 2)),
    ("k", (3, 1, 2, 0)),
    ("l", (3, 2, 0, 1)),

]

EO_DATA = [
    ("0", (1, 1, 1, 1)),
    ("1", (0, 1, 0, 1)),
    ("2", (1, 0, 1, 0)),
    ("4", (0, 0, 0, 0)),
    ("6", (0, 0, 1, 1)),
    ("7", (1, 0, 0, 1)),
    ("8", (1, 1, 0, 0)),
    ("9", (0, 1, 1, 0)),
]

# TODO: explain why quadruples
CP_DATA = [
    ("o", (0, 1, 2, 3)),
    ("d", (0, 3, 2, 1)),
    ("b", (0, 3, 1, 2)),   # crazy
    # ("b", (1, 0, 2, 3)), # naive
    # ("b", (3, 1, 0, 2)),
    # ("b", (2, 3, 1, 0)),
    # ("l", (2, 0, 3, 1)),
    # ("l", (1, 2, 0, 3)),
    # ("l", (3, 1, 2, 0)), # naive
    ("l", (0, 2, 3, 1)),   # crazy
    ("r", (0, 2, 1, 3)),
    ("f", (0, 1, 3, 2)),
]
CO_DATA = [
    ("A", (0, 0, 0, 0)),
    ("B", (0, 2, 2, 2)),
    ("b", (0, 1, 1, 1)),
    ("C", (0, 0, 1, 2)),
    ("D", (0, 0, 2, 1)),
    ("E", (0, 1, 0, 2)),
    ("F", (1, 2, 1, 2)),
    ("G", (1, 1, 2, 2)),
]


def _decode_po(data, ch):
    for ix, _ in enumerate(data):
        ch2, iv = data[ix]
        if ch == ch2:
            return iv
    return -1


def decode(cls, prid):
    ep, eo = [], []
    cp, co = [], []
    solved = cls.new()

    co = _decode_po(CO_DATA, prid[0])
    co += solved.CORNERS.orientation[4:]
    cp = _decode_po(CP_DATA, prid[1])
    cp += solved.CORNERS.permutation[4:]
    eo = _decode_po(EO_DATA, prid[2])
    eo += solved.EDGES.orientation[4:]
    ep = _decode_po(EP_DATA, prid[3])
    ep += solved.EDGES.permutation[4:]

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
            "permutation": solved.CENTERS.permutation,
            "orientation": solved.CENTERS.orientation,
        },
    })


def _encode_po(data, p):
    for ch, p2 in data:
        if tuple(p2) == tuple(p):
            return ch
    return "?"


def encode(cls, pos):
    if not isinstance(pos, cls):
        raise TypeError("input must be a {} object".format(cls.__name__))

    # TODO assert is_ll
    prid = ''.join([
        _encode_po(CO_DATA, pos.CORNERS.orientation[0:4]),
        _encode_po(CP_DATA, pos.CORNERS.permutation[0:4]),
        _encode_po(EO_DATA, pos.EDGES.orientation[0:4]),
        _encode_po(EP_DATA, pos.EDGES.permutation[0:4])])

    return prid


def orid_from_prid(birdflu_prid):  # Ao4A -> A_4_
    orid = "{}_{}_".format(
        birdflu_prid[0],
        birdflu_prid[2])
    return orid
