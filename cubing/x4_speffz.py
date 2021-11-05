from .kpuzzle.trans import BaseTransform
from .stickers.display import DisplayMixin


@BaseTransform.transform
class Transform(DisplayMixin):
    ksolve_filename = "4x4x4-speffz.tws"
    num_slices = 4

    
# ```
# from cubing.kpuzzle.orbit import Orbit
# from cubing.kpuzzle.puzdef import PuzDef
# from cubing.x4 import Transform as X4
# from cubing.x4_speffz import Transform as X4SP, TO_SPEFFZ_D
# 
# r2s = X4.from_dict(TO_SPEFFZ_D)
# solved = X4.from_dict(X4SP.kpuzzle.startPieces)
# x4_pd = PuzDef.from_ksolve("4x4x4-reidish.tws")
# x4sp_pd = PuzDef.from_ksolve("4x4x4-speffz.tws")
# Orbit.convert_trans(
#     X4,
#     X4.from_dict(x4_pd.solvedString),    # FROM REID
#     X4.from_dict(x4sp_pd.solvedString),  # TO SPEFFZ
#     orbits=X4.kpuzzle.orbits)(solved) == r2s
# ```
TO_SPEFFZ_D = {
  "EDGES2": {
    "permutation": [
        2, 1, 0, 3, 13, 9, 21, 17,
        12, 8, 20, 16, 14, 10, 22, 18,
        15, 11, 23, 19, 5, 4, 7, 6],
    "orientation": [
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0]
  },
  "CORNERS": {
    "permutation": [2, 1, 0, 3, 5, 4, 7, 6],
    "orientation": [0, 0, 0, 0, 0, 0, 0, 0]
  },
  "CENTERS3": {
    "permutation": [
        2, 1, 0, 3, 13, 9, 21, 17,
        12, 8, 20, 16, 14, 10, 22, 18,
        15, 11, 23, 19, 5, 4, 7, 6],
    "orientation": [
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0]
  }
}
