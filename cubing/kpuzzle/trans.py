import six
from collections import namedtuple
from .orbit import Orbit
from .puzdef import PuzDef


class BaseTransform:
    is_active = False
    kpuzzle = None
    ksolve_filename = None
    move_cache = None
    num_slices = 0
    solved = None

    def __getstate__(self):
        # _asdict() is a method provided by namedtuple
        return dict((k, v._asdict())
                    for k, v in self._asdict().items())

    def __call__(self, other):
        # https://github.com/cubing/twsearch/blob/main/ksolveformat.txt
        return type(self).from_dict(
            Orbit.multiply_all(
                other._asdict(),
                self._asdict(),
                orbits=type(self).kpuzzle.orbits)
            if self.is_active else
            Orbit.multiply_all(
                self._asdict(),
                other._asdict(),
                orbits=type(self).kpuzzle.orbits)
        )
    
    def __matmul__(self, other):
        return self.__call__(other)

    def __pow__(self, other):
        raise NotImplementedError
    
    def __neg__(self):
        return type(self).from_dict(
            Orbit.inverse_all(
                self._asdict(),
                orbits=type(self).kpuzzle.orbits))

    def is_solved(self):
        return tuple(self) == tuple(type(self).new())

    @classmethod
    def new(cls):
        return cls.from_dict(dict([
            (oname, Orbit.new(orbit["numPieces"]))
            for oname, orbit in cls.kpuzzle.orbits.items()]))

    @classmethod
    def from_orbitdefs(cls, orbits):
        d = dict([
            (oname, Orbit.from_orbitdef(orbit))
            for oname, orbit in orbits.items()
        ])
        return cls.from_dict(d)

    @classmethod
    def from_dict(cls, trans):
        # The schema for the dictionary data
        # is the KPUZZLE draft standard available at
        # https://standards.cubing.net/draft/3/kpuzzle/
        # print(repr(trans))
        corner_keys = [k for k in trans.keys() if k[0:2] == 'CO']
        if len(corner_keys) and isinstance(trans[corner_keys[0]], Orbit):
            return cls(**trans)
        else:
            d = dict([
                (oname, Orbit.new(orbit["numPieces"]))
                for oname, orbit in cls.orbit_defs.items()])
            d.update(dict(
                (oname, Orbit.from_dict(
                    orbit_spaces, cls.orbit_defs[oname]["numPieces"]))
                for oname, orbit_spaces in trans.items()))
            return cls(**d)

    # @classmethod
    # def from_solved_string(cls, trans):
    #     # The schema for the dictionary data
    #     # is the KPUZZLE draft standard available at
    #     # https://standards.cubing.net/draft/3/kpuzzle/
    #     # print(repr(trans))
    #     return cls(**dict(
    #         (orbit, Orbit(
    #             permutation=tuple(orbit_spaces['permutation']),
    #             orientation=None))
    #         for orbit, orbit_spaces in trans.items()))

    @classmethod
    def from_alg(cls, steps):
        """
        Performs the alg "(steps)"
        """
        # print(repr(steps))
        assert isinstance(steps, six.string_types)
        self = cls.new()
        for step in steps.split(' '):
            try:
                # multiply self = self*other
                other = cls.move_cache[step]
                self = self(other)
            except Exception as exc:
                print(repr(exc))
                raise
        return self

    @classmethod
    def transform(base_cls2, cls):
        if not cls.num_slices:
            raise ValueError("num_slices is required")
        if getattr(cls, 'ksolve_filename', None) \
           and not getattr(cls, 'kpuzzle', None):
            cls.kpuzzle = PuzDef.from_ksolve(cls.ksolve_filename)
        if getattr(cls, 'kpuzzle_filename', None) \
           and not getattr(cls, 'kpuzzle', None):
            cls.kpuzzle = PuzDef.from_kpuzzle(cls.kpuzzle_filename)

        base_cls1 = namedtuple(
            'BaseTransform',
            list(reversed(sorted(
                cls.kpuzzle.orbits.keys()))))

        class transform_cls(base_cls1, base_cls2, cls):
            move_cache = dict()
            kpuzzle = cls.kpuzzle
            move_defs = cls.kpuzzle.moves
            orbit_defs = cls.kpuzzle.orbits
            num_slices = cls.num_slices
            is_active = cls.is_active if getattr(
                cls, 'is_active', False) else False

        # transform_cls.start_pieces = transform_cls.new()
        transform_cls.init_moves()
        transform_cls.__name__ = cls.__name__
        return transform_cls

    @classmethod
    def init_moves(cls):
        if getattr(cls, 'ksolve_filename', None) \
           and not getattr(cls, 'kpuzzle', None):
            cls.kpuzzle = PuzDef.from_ksolve(cls.ksolve_filename)
        if getattr(cls, 'kpuzzle_filename', None) \
           and not getattr(cls, 'kpuzzle', None):
            cls.kpuzzle = PuzDef.from_kpuzzle(cls.kpuzzle_filename)
        if cls.move_cache is None:
            cls.move_cache = {}
        cls.move_cache[""] = cls.new()
        for move, move_transform in cls.kpuzzle.moves.items():
            cls.move_cache[move] = cls.from_dict(move_transform)
            cls.move_cache[move + "2"] = cls.from_alg(
                "{} {}".format(move, move))
            cls.move_cache[move + "3"] = cls.from_alg(
                "{} {} {}".format(move, move, move))
            cls.move_cache[move + "3'"] = cls.from_alg(
                "{} {} {}".format(move, move, move)).__neg__()
            cls.move_cache[move + "2'"] = cls.from_alg(
                "{} {}".format(move, move)).__neg__()
            cls.move_cache[move + "'"] = cls.from_alg(
                "{}".format(move)).__neg__()

    def reclass(self, cls):
        return cls.from_dict(self.__getstate__())

    def copy(self):
        return self.reclass(type(self))

    def alg(self, steps):
        """
        Performs the alg "(self) (steps)"
        """
        return self.__call__(type(self).from_alg(steps))

    def rotate(self, steps):
        """
        Performs the alg "(steps)' (self) (steps)"
        """
        return self.__neg__().alg(steps).__neg__().alg(steps)

    def conjugate(self, other):
        """
        Performs the alg "(other)' (self) (other)"
        """
        return self.__neg__()(other).__neg__()(other)

    def to_json(self):
        import json
        from ..ksolve.reflow import json_reflow
        return json_reflow(json.dumps(self.__getstate__(), indent=2))

    def json(self):
        print(self.to_json())
        return self

    def to_ksolve(self, header="Move", header_name="A", nocenter=True):
        from ..ksolve.reflow import ksolve_script
        return ksolve_script(
            self.__getstate__(),
            header=header,
            header_name=header_name,
            nocenter=nocenter)

    def ksolve(self, header="Move", header_name="A", nocenter=True):
        print(self.to_ksolve(header=header,
                             header_name=header_name,
                             nocenter=nocenter))
        return self

    @classmethod
    def from_ksolve(cls, reader, header=None):
        from ..ksolve.puzdef import parse_reader
        results = parse_reader(reader)
        return cls.from_dict(list(results[0][header].items())[0][1])
        
    def invert_centers(self):
        return self._replace(
            CENTERS=self.CENTERS._replace(
                orientation=tuple((4 - i) % 4
                                  for i in self.CENTERS.orientation)))

    def invert_corners(self):
        return self._replace(
            CORNERS=self.CORNERS._replace(
                orientation=tuple((3 - i) % 3
                                  for i in self.CORNERS.orientation)))

    def match_old(self, solved, pattern, orbits=None):
        if orbits is None:
            orbits = self.kpuzzle.orbits
        for orbit_name in orbits.keys():
            if not getattr(self, orbit_name).match_old(
                    getattr(solved, orbit_name),
                    getattr(pattern, orbit_name)):
                return False
        return True

    
    def match(self, solved, orbits=None):
        """
        This implementation must match
        <https://github.com/Cride5/visualcube/blob/master/cube_lib.php#L964>
        which suppoorts (-1) as a wildcard.

        This implementation shouldn't match
        <https://github.com/cubing/twsearch/blob/main/src/puzdef.h#L102>
        which doesn't support (-1).
        """
        if orbits is None:
            orbits = self.kpuzzle.orbits
        for orbit_name in orbits.keys():
            if not getattr(self, orbit_name).match(
                    getattr(solved, orbit_name)):
                return False
        return True
