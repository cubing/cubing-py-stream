"""
The Transform in this file represents an example 2x2x2
cube puzzle in Reid order.
"""
from .kpuzzle.trans import BaseTransform
from .stickers.display import DisplayMixin


@BaseTransform.transform
class Transform(DisplayMixin):
    ksolve_filename = "2x2x2-reid.tws"
    num_slices = 2
