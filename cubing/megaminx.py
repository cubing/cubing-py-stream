from .kpuzzle.trans import BaseTransform


@BaseTransform.transform
class Transform:
    ksolve_filename = "megaminx-reidish.tws"
    num_slices = 3
