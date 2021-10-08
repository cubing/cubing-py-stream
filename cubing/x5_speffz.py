from .kpuzzle.trans import BaseTransform
from .stickers.display import DisplayMixin


@BaseTransform.transform
class Transform(DisplayMixin):
    ksolve_filename = "5x5x5-speffz.tws"
    num_slices = 5


# ```
# from cubing.kpuzzle.orbit import Orbit
# from cubing.kpuzzle.puzdef import PuzDef
# from cubing.x5 import Transform as X5
# from cubing.x5_speffz import Transform as X5SP, TO_SPEFFZ_D
# 
# r2s = X5.from_dict(TO_SPEFFZ_D)
# solved = X5.from_dict(X5SP.kpuzzle.startPieces)
# x5_pd = PuzDef.from_ksolve("5x5x5-reidish.tws")
# x5sp_pd = PuzDef.from_ksolve("5x5x5-speffz.tws")
# Orbit.convert_trans(
#     X5,
#     X5.from_dict(x5_pd.solvedString),    # FROM REID
#     X5.from_dict(x5sp_pd.solvedString),  # TO SPEFFZ
#     orbits=X5.kpuzzle.orbits)(solved) == r2s
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
  "EDGES": {
    "permutation": [2, 1, 0, 3, 9, 8, 10, 11, 4, 5, 6, 7],
    "orientation": [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
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
  },
  "CENTERS2": {
    "permutation": [
        2, 1, 0, 3, 13, 9, 21, 17,
        12, 8, 20, 16, 14, 10, 22, 18,
        15, 11, 23, 19, 5, 4, 7, 6],
    "orientation": [
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0]
  },
  "CENTERS": {
    "permutation": [0, 1, 2, 3, 4, 5],
    "orientation": [0, 0, 0, 0, 0, 0]
  }
}
