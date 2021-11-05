import os.path
import pandas
from .stickers_base import _get_is_at
from ..kpuzzle.trans import BaseTransform


def decode(s, numSlices=3, orbitDefs=None, solvedString=None):
    pass


def encode(pos, numSlices=3, orbitDefs=None, solvedString=None):
    assert isinstance(pos, BaseTransform)
    lines = [
        bytearray(("{0:" + str(4*numSlices) +
                   "s}").format(" ").encode('latin1'))
        for _ in range(3*numSlices)]

    stickers = pandas.read_csv(os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "puzzles", "{n}x{n}x{n}-display.csv".format(n=numSlices)), dtype=str)

    # TODO, fix this
    if type(pos).is_active:
        # pos = pos.__neg__()
        # is_active = False
        raise ValueError(
            "Active Permutations should be " +
            "handled primarily by the Orbit class")
    # else:
    #     is_active = False

    for orbit, orbit_t in orbitDefs.items():
        numPieces = orbit_t["numPieces"]
        orientations = orbit_t["orientations"]
        if orbit.startswith('CE'):
            orientations = 1
        if orbit.startswith('ED'):
            orientations = 2
        for piece_num in range(0, numPieces):
            is_at_data = _get_is_at(
                piece_num,
                getattr(pos, orbit).orientation,
                getattr(pos, orbit).permutation,
                solvedString[orbit]['permutation'],
                is_active=False,
                orientations=orientations,
                stickers=stickers)
            for facelet, x, y in is_at_data:
                lines[y][x] = ord(facelet)

    s = '\n'.join([line.decode('latin1') for line in lines])
    return s
