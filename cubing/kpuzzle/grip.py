from collections import namedtuple

BaseGrip = namedtuple("BaseGrip", "dim grip name")


class Grip(BaseGrip):
    layer_cache = []
    layers = "BSFDEULMR"
    faces = "ULFRBD"
    dims = "xyz"

    @classmethod
    def init_layers(cls):
        cls.layer_cache += [
            cls(-1, "z", "B"),
            cls(1, "z", "F"),
            cls(-1, "y", "D"),
            cls(1, "y", "U"),
            cls(-1, "x", "L"),
            cls(1, "x", "R"),
        ]

    @classmethod
    def get_dim(cls, dim_name):
        results = [layer for layer in cls.layer_cache
                   if layer.dim == dim_name]
        return results[0] if len(results) else None

    @classmethod
    def get_layer(cls, layer_name):
        print(repr(layer_name))
        # todo, strip numbers and quotes from the end
        layer_name = layer_name[0]
        results = [layer for layer in cls.layer_cache
                   if layer.name == layer_name]
        return results[0] if len(results) else None

    @classmethod
    def is_opp(cls, side, side2):
        layer = cls.get_layer(side)
        layer2 = cls.get_layer(side2)
        if layer and layer2:
            return layer.dim == layer2.dim
        elif side in cls.dims:
            return layer2.dim == side
        elif side2 in cls.dims:
            return layer.dim == side2
        else:
            return False


Grip.init_layers()
