"""
The Transform in this file represents an example 3x3x3
cube puzzle in Speffz order.
"""
from .kpuzzle.trans import BaseTransform
from .stickers.display import DisplayMixin
from .x3_formats.mixin import X3FormatsMixin


@BaseTransform.transform
class Transform(DisplayMixin, X3FormatsMixin):
    ksolve_filename = "3x3x3-speffz.tws"
    num_slices = 3


X3FormatsMixin.init_x3(Transform)


# This assumes passive permutations.
# This converts a position A (in Reid order)
# to a position B (in Speffz order) with the formula:
#
#   (ToSpeffz)' A (ToSpeffz) = B
#
# This can be calculated with the Python code:
#
# ```
# from cubing.kpuzzle.orbit import Orbit
# from cubing.kpuzzle.puzdef import PuzDef
# from cubing.x3 import Transform as X3
# from cubing.x3_speffz import Transform as X3SP, TO_SPEFFZ_D
# 
# r2s = X3.from_dict(TO_SPEFFZ_D)
# solved = X3.from_dict(X3SP.kpuzzle.startPieces)
# x3_pd = PuzDef.from_ksolve("3x3x3-reid.tws")
# x3sp_pd = PuzDef.from_ksolve("3x3x3-speffz.tws")
# Orbit.convert_trans(
#     X3,
#     X3.from_dict(x3_pd.solvedString),    # FROM REID
#     X3.from_dict(x3sp_pd.solvedString),  # TO SPEFFZ
#     orbits=X3.kpuzzle.orbits)(solved) == r2s
# ```
TO_SPEFFZ_D = {
  "EDGES": {
    "permutation": [2, 1, 0, 3, 9, 8, 10, 11, 4, 5, 6, 7],
    "orientation": [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
  },
  "CORNERS": {
    "permutation": [2, 1, 0, 3, 5, 4, 7, 6],
    "orientation": [0, 0, 0, 0, 0, 0, 0, 0]
  },
  "CENTERS": {
    "permutation": [0, 1, 2, 3, 4, 5],
    "orientation": [0, 0, 0, 0, 0, 0]
  }
}
