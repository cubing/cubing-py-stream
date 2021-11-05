"""
The Transform in this file represents an example 4x4x4
cube puzzle in Reid-ish order. Michael Reid only defined
an order for 3x3x3 cube puzzles, but this extends that
definition to 4x4x4.
"""
from .kpuzzle.trans import BaseTransform
from .stickers.display import DisplayMixin


@BaseTransform.transform
class Transform(DisplayMixin):
    ksolve_filename = "4x4x4-reidish.tws"
    num_slices = 4
