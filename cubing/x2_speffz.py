from .kpuzzle.trans import BaseTransform
from .stickers.display import DisplayMixin


@BaseTransform.transform
class Transform(DisplayMixin):
    ksolve_filename = "2x2x2-speffz.tws"
    num_slices = 2


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
# from cubing.x2 import Transform as X2
# from cubing.x2_speffz import Transform as X2SP, TO_SPEFFZ_D
# 
# r2s = X2.from_dict(TO_SPEFFZ_D)
# solved = X2.from_dict(X2SP.kpuzzle.startPieces)
# x2_pd = PuzDef.from_ksolve("2x2x2-reid.tws")
# x2sp_pd = PuzDef.from_ksolve("2x2x2-speffz.tws")
# Orbit.convert_trans(
#     X2,
#     X2.from_dict(x2_pd.solvedString),    # FROM REID
#     X2.from_dict(x2sp_pd.solvedString),  # TO SPEFFZ
#     orbits=X2.kpuzzle.orbits)(solved) == r2s
# ```
TO_SPEFFZ_D = {
  "CORNERS": {
    "permutation": [2, 1, 0, 3, 5, 4, 7, 6],
    "orientation": [0, 0, 0, 0, 0, 0, 0, 0]
  }
}
