"""
The Transform in this file represents an example 3x3x3
cube puzzle in Reid order.
"""
from .kpuzzle.trans import BaseTransform
from .stickers.display import DisplayMixin
from .x3_formats.mixin import X3FormatsMixin


@BaseTransform.transform
class Transform(DisplayMixin, X3FormatsMixin):
    ksolve_filename = "3x3x3-reid.tws"
    num_slices = 3


X3FormatsMixin.init_x3(Transform)
