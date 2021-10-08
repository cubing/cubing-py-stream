from .birdflu_ll_pos import (
    EO_DATA,
    # decode as birdflu_decode,
    encode as birdflu_encode)

COP_TAB = [
    ("Ad", "aiai"),
    ("Af", "aaeo"),
    ("Ao", "aaaa"),
    ("Bb", "akqq"),
    ("Bd", "akck"),
    ("Bf", "acgq"),
    ("Bl", "aggk"),
    ("Bo", "accc"),
    ("Br", "agqc"),
    ("Cb", "aipq"),
    ("Cd", "aibk"),
    ("Cf", "aafq"),
    ("Cl", "aefk"),
    ("Co", "aabc"),
    ("Cr", "aepc"),
    ("Db", "aiqp"),
    ("Dd", "aicj"),
    ("Df", "aagp"),
    ("Dl", "aegj"),
    ("Do", "aacb"),
    ("Dr", "aeqb"),
    ("Eb", "ajoq"),
    ("Ed", "ajak"),
    ("Ef", "abeq"),
    ("El", "afek"),
    ("Eo", "abac"),
    ("Er", "afoc"),
    ("Fd", "bkbk"),
    ("Ff", "bcfq"),
    ("Fl", "bgfk"),
    ("Fo", "bcbc"),
    ("Gb", "bjqq"),
    ("Gd", "bjck"),
    ("Gf", "bbgq"),
    ("Gl", "bfgk"),
    ("Go", "bbcc"),
    ("Gr", "bfqc"),
    ("bb", "ajpp"),
    ("bd", "ajbj"),
    ("bf", "abfp"),
    ("bl", "affj"),
    ("bo", "abbb"),
    ("br", "afpb"),
]

EP_TAB = [
    ("A", "1111"),
    ("B", "5555"),
    ("C", "7373"),
    ("D", "3737"),
    ("E", "1335"),
    ("F", "1577"),
    ("G", "5133"),
    ("H", "7157"),
    ("I", "3513"),
    ("J", "7715"),
    ("K", "3351"),
    ("L", "5771"),
    ("a", "7777"),
    ("b", "3333"),
    ("c", "1515"),
    ("d", "5151"),
    ("e", "3711"),
    ("f", "5735"),
    ("g", "1371"),
    ("h", "5573"),
    ("i", "1137"),
    ("j", "3557"),
    ("k", "7113"),
    ("l", "7355"),
]


def decode(cls, ps):
    pass


def encode(cls, pos):
    if not isinstance(pos, cls):
        raise TypeError("input must be a {} object".format(cls.__name__))

    prid = birdflu_encode(cls, pos)
    cop = dict(COP_TAB)[prid[0:2]]
    ep = dict(EP_TAB)[prid[3]]
    eo = dict(EO_DATA)[prid[2]]
    eop = bytearray(ep, 'latin1')
    for i in range(4):
        eop[i] += eo[i]
    eop = bytes(eop).decode('latin1')

    return "{}{}{}{}{}{}{}{}".format(
        cop[0], eop[0],
        cop[1], eop[1],
        cop[2], eop[2],
        cop[3], eop[3])
