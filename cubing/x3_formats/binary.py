# BEGIN STOLEN FROM https://github.com/cubing/binary3x3x3-c
popcount64 = [
    0, 1, 1, 2, 1, 2, 2, 3,
    1, 2, 2, 3, 2, 3, 3, 4,
    1, 2, 2, 3, 2, 3, 3, 4,
    2, 3, 3, 4, 3, 4, 4, 5,
    1, 2, 2, 3, 2, 3, 3, 4,
    2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5,
    3, 4, 4, 5, 4, 5, 5, 6]


def _encode_perm(a, n):
    bits = 0
    r = 0
    for i in range(0, n):
        bits |= 1 << a[i]
        low = ((1 << a[i]) - 1) & bits
        r = r * (n-i) + a[i] - popcount64[low >> 6] - popcount64[low & 63]
    if (bits + 1 != 1 << n):
        return -1
    return r


def _decode_perm(lex, n):
    a = [0 for _ in range(n)]

    # last element of list
    a[n-1] = 0

    # iterate from 2nd-to-last element
    # until the first element of list
    for i in range(n - 2, 0 - 1, -1):

        # divmod
        a[i] = lex % (n - i)
        lex = int(lex / (n - i))

        for j in range(i + 1, n):
            if (a[j] >= a[i]):
                a[j] += 1
    return list(map(int, a))
# END STOLEN FROM https://github.com/cubing/binary3x3x3-c


# A database of all entire cube orientations
MODB = [
    # PO_U, PO_L, CENTERS.perm, alg
    (0, 0, (0, 1, 2, 3, 4, 5), ""),
    (0, 1, (0, 2, 3, 4, 1, 5), "y"),
    (0, 2, (0, 3, 4, 1, 2, 5), "y2"),
    (0, 3, (0, 4, 1, 2, 3, 5), "y'"),
    (1, 0, (1, 0, 4, 5, 2, 3), "x y' x"),       # y2 z'
    (1, 1, (1, 2, 0, 4, 5, 3), "y x'"),
    (1, 2, (1, 4, 5, 2, 0, 3), "y' x"),
    (1, 3, (1, 5, 2, 0, 4, 3), "x y x'"),       # z
    (2, 0, (2, 0, 1, 5, 3, 4), "x y'"),
    (2, 1, (2, 1, 5, 3, 0, 4), "x"),
    (2, 2, (2, 3, 0, 1, 5, 4), "x y2"),
    (2, 3, (2, 5, 3, 0, 1, 4), "x y"),
    (3, 0, (3, 0, 2, 5, 4, 1), "x y' x'"),      # z'
    (3, 1, (3, 2, 5, 4, 0, 1), "y x"),
    (3, 2, (3, 4, 0, 2, 5, 1), "y' x'"),
    (3, 3, (3, 5, 4, 0, 2, 1), "x y x"),        # y2 z
    (4, 0, (4, 0, 3, 5, 1, 2), "x' y"),
    (4, 1, (4, 1, 0, 3, 5, 2), "x'"),
    (4, 2, (4, 3, 5, 1, 0, 2), "x' y2"),
    (4, 3, (4, 5, 1, 0, 3, 2), "x' y'"),
    (5, 0, (5, 1, 4, 3, 2, 0), "x2"),           # y2 z2
    (5, 1, (5, 2, 1, 4, 3, 0), "x2 y'"),
    (5, 2, (5, 3, 2, 1, 4, 0), "x2 y2"),        # z2
    (5, 3, (5, 4, 3, 2, 1, 0), "x2 y"),
]


def _decode_pad(ls, n):
    return [0 for _ in range(n - len(ls))] + ls


def _decode_reid(cls, d):
    import numpy
    ep = d['EP']
    eo = d['EO']
    cp = d['CP']
    co = d['CO']
    po_u = d['PO_U']
    po_l = d['PO_L']
    for u, l, cperm, _ in MODB:
        if po_u == u and po_l == l:
            mp = cperm
            break
    else:
        mp = [i for i in range(6)]
    # mo_q = d['MO_Q']
    mo = d['MO']
    eo = _decode_pad(list(map(
        int, list(numpy.base_repr(eo, 2)))), 12)
    co = _decode_pad(list(map(
        int, list(numpy.base_repr(co, 3)))), 8)
    mo = _decode_pad(list(map(
        int, list(numpy.base_repr(mo, 4)))), 6)

    d2 = {
        'EDGES': {
            'permutation': _decode_perm(ep, 12),
            'orientation': eo,
        },
        'CORNERS': {
            'permutation': _decode_perm(cp, 8),
            'orientation': co,
        },
        'CENTERS': {
            'permutation': tuple(mp),
            'orientation': mo,
        }
    }
    return cls.from_dict(d2)


def _decode_unhexlify(bs):
    import binascii
    bs = bs.replace(' ', '')
    bs = binascii.unhexlify(bs)
    return bs


def _encode_hexlify(bs):
    return ' '.join(map(lambda x: "{:02x}".format(x), bs))


def _encode_reid(cls, pos, mo_q=False):
    ep = pos.EDGES.permutation
    ep = _encode_perm(ep, 12)
    eo = pos.EDGES.orientation
    eo = int(''.join([str(v) for v in eo]), 2)
    cp = pos.CORNERS.permutation
    cp = _encode_perm(cp, 8)
    co = pos.CORNERS.orientation
    co = int(''.join([str(v) for v in co]), 3)
    mp = pos.CENTERS.permutation
    po_u = mp.index(0)
    po_l = 0
    for u, l, cperm, _ in MODB:
        if cperm == mp:
            po_l = l
    mo = pos.CENTERS.orientation
    mo = int(''.join(["{:#04b}".format(v)[2:] for v in mo]), 2)
    d = {
        'EP': ep,
        'EO': eo,
        'CP': cp,
        'CO': co,
        'PO_U': po_u if mo_q else 7,
        'PO_L': po_l if mo_q else 0,
        'MO_Q': mo_q,
        'MO': mo if mo_q else 0,
    }
    return d


def _decode_to_dict(bs):
    ep = (bs[0] << 21) | \
        (bs[1] << 13) | \
        (bs[2] << 5) | \
        ((bs[3] >> 3) & 0x3f)
    eo = ((bs[3] & 0x7) << 9) | \
        (bs[4] << 1) | \
        ((bs[5] & 0x80) >> 7)
    cp = ((bs[5] & 0x7f) << 9) | \
        (bs[6] << 1) | \
        ((bs[7] & 0x80) >> 7)
    co = ((bs[7] & 0x7f) << 6) | \
        ((bs[8] >> 2) & 0x3f)
    po_u = ((bs[8] & 0x3) << 1) | \
        ((bs[9] >> 7) & 0x1)
    po_l = (bs[9] >> 5) & 0x3
    mo_q = ((bs[9] >> 4) & 0x1) == 1
    mo = ((bs[9] & 0xf) << 8) | \
        (bs[10])
    return {
        'EP': ep,
        'EO': eo,
        'CP': cp,
        'CO': co,
        'PO_U': po_u,
        'PO_L': po_l,
        'MO_Q': mo_q,
        'MO': mo if mo_q else 0,
    }


def _encode_from_dict(d):
    ep = d['EP']
    eo = d['EO']
    cp = d['CP']
    co = d['CO']
    po_u = d['PO_U']
    po_l = d['PO_L']
    mo_q = d['MO_Q']
    mo = d['MO']
    bs = [0 for i in range(11)]

    bs[0] = (ep >> 21) & 0xff
    bs[1] = (ep >> 13) & 0xff
    bs[2] = (ep >> 5) & 0xff
    bs[3] = (ep << 3) & 0xff
    bs[3] |= (eo >> 9) & 0xff
    bs[4] = (eo >> 1) & 0xff
    bs[5] = (eo << 7) & 0xff
    bs[5] |= (cp >> 9) & 0xff
    bs[6] = (cp >> 1) & 0xff
    bs[7] = (cp << 7) & 0xff
    bs[7] |= (co >> 6) & 0xff
    bs[8] = (co << 2) & 0xff
    bs[8] |= (po_u >> 1) & 0xff
    bs[9] = (po_u << 7) & 0xff
    bs[9] |= (po_l << 5) & 0xff
    bs[9] |= ((1 if mo_q else 0) << 4)
    bs[9] |= (mo >> 8) & 0xff
    bs[10] |= (mo) & 0xff

    return bytes(bs)


def decode(cls, s):

    # hex-string to byte-string
    bs = _decode_unhexlify(s)

    # byte-string to reid internals
    d = _decode_to_dict(bs)
    pos = _decode_reid(cls, d)

    # convert reid to speffz
    conv = pos
    # conv = utils.convert_to_puzzle(
    #     pos,
    #     ksolve_puzdef["pieces"],
    #     speffz_puzdef["pieces"])

    return conv


def encode(cls, pos, mo=False):

    # convert speffz to reid
    conv = pos
    # conv = utils.convert_to_puzzle(
    #     pos,
    #     speffz_puzdef["pieces"],
    #     ksolve_puzdef["pieces"])

    # convert reid internals to byte-string
    d = _encode_reid(cls, conv, mo_q=mo)
    bs = _encode_from_dict(d)

    # convert byte-string to hex-string
    s = _encode_hexlify(bs)

    return s


def _decode_d(cls, comp, mo=False):
    d = {
        "EP": comp["epLex"],
        "EO": comp["eoMask"],
        "CP": comp["cpLex"],
        "CO": comp["coMask"],
        "PO_U": comp["poIdxU"],
        "PO_L": comp["poIdxL"],
        "MO_Q": comp["moSupport"],
        "MO": comp["moMask"],
    }
    return _decode_reid(cls, d)


def _encode_d(cls, pos, mo=False):
    """
        {
          "epLex": 7257600,
          "eoMask": 1536,
          "cpLex": 5160,
          "coMask": 1215,
          "poIdxU": 0,
          "poIdxL": 2,
          "moSupport": 1,
          "moMask": 0
        }
    """
    d = _encode_reid(cls, pos, mo_q=mo)
    return {
        "epLex": d["EP"],
        "eoMask": d["EO"],
        "cpLex": d["CP"],
        "coMask": d["CO"],
        "poIdxU": d["PO_U"],
        "poIdxL": d["PO_L"],
        "moSupport": d["MO_Q"],
        "moMask": d["MO"],
    }
