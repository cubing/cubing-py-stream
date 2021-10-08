from collections import namedtuple

# KPuzzle calls this "Orbit Definition"
BaseOrbitDef = namedtuple('OrbitDef', 'numPieces orientations')

# KPuzzle calls this "Orbit Transformation"
BaseOrbit = namedtuple('Orbit', 'permutation orientation')


class Orbit(BaseOrbit):

    def __getstate__(self):
        return self._asdict()

    @classmethod
    def new(cls, numPieces):
        return cls.from_dict(dict([
            ("permutation", tuple([i for i in range(numPieces)])),
            ("orientation", tuple([0 for i in range(numPieces)])),
        ]), numPieces)

    @classmethod
    def from_dict(cls, orbit, numPieces=None):
        if 'orientation' not in orbit or not orbit['orientation']:
            orbit['orientation'] = tuple([0 for i in range(numPieces)])
        orbit['permutation'] = tuple(orbit['permutation'])
        orbit['orientation'] = tuple(orbit['orientation'])
        return cls(**orbit)

    @classmethod
    def from_orbitdef(cls, orbit):
        numPieces = orbit["numPieces"]
        d = {
            "permutation": [i for i in range(numPieces)],
            "orientation": [0 for i in range(numPieces)],
        }
        return cls.from_dict(d)

    def validate(self, numPieces=None, orientations=None):
        assert numPieces is not None
        assert isinstance(self.permutation, tuple), type(self.permutation)
        assert isinstance(self.orientation, tuple), type(self.orientation)
        assert len(self.permutation) == numPieces, len(self.permutation)
        assert len(self.orientation) == numPieces, len(self.orientation)
        for i, ori in enumerate(self.orientation):
            assert 0 <= ori and ori < orientations, \
                "bad orientation: {}/{}".format(
                    ori, orientations)
        return self

    def inverse(self, numPieces=None, orientations=None):
        try:
            return type(self)(
                permutation=tuple(
                    self.permutation.index(piece)
                    for piece in range(numPieces)),
                orientation=tuple(
                    (-self.orientation[
                        self.permutation.index(piece)]) % orientations
                    for piece in range(numPieces)))
        except Exception as exc:
            print(repr(exc), repr(self), repr(numPieces), repr(orientations))
            raise exc

    def multiply(self, other, numPieces=None, orientations=None):
        return Orbit(
            permutation=tuple(
                self.permutation[other.permutation[piece]]
                for piece in range(numPieces)),
            orientation=tuple(
                (self.orientation[other.permutation[piece]] +
                 other.orientation[piece]) % orientations
                for piece in range(numPieces)))

    @classmethod
    def inverse_all(cls, state1, orbits=None):
        assert isinstance(state1, dict)
        state2 = dict()

        for orbit in orbits.keys():
            assert isinstance(state1[orbit], Orbit)
            state1[orbit].validate(**orbits[orbit])
            if orbit not in state2.keys():
                state2[orbit] = dict()

            state2[orbit] = state1[orbit].inverse(**orbits[orbit])

        return state2

    @classmethod
    def multiply_all(cls, state1, state2, orbits=None):
        assert isinstance(state1, dict)
        assert isinstance(state2, dict)
        state3 = dict()

        for orbit in orbits.keys():
            assert isinstance(state1[orbit], Orbit)
            assert isinstance(state2[orbit], Orbit)
            state1[orbit].validate(**orbits[orbit])
            state2[orbit].validate(**orbits[orbit])
            if orbit not in state3.keys():
                state3[orbit] = dict()

            state3[orbit] = state1[orbit].multiply(
                state2[orbit], **orbits[orbit])

        return state3

    @classmethod
    def find_orientation(
            cls, name1, name2,
            negate=False,
            numPieces=None,
            orientations=None):
        if tuple(name1) == tuple(name2):
            return 0
        elif orientations == 2:
            print(name1, name2)
            if tuple(name1[0:2]) == tuple([name1[1], name1[0]]):
                return 1
            else:
                raise ValueError("Please use eoNegate = True")
        elif orientations == 3:
            if tuple(name1[0:2]) == tuple([name1[1], name1[2], name1[0]]):
                return 1
            elif tuple(name1[0:2]) == tuple([name1[2], name1[0], name1[1]]):
                return 2
            else:
                raise ValueError("Please use coNegate = True")
        else:
            raise ValueError("corners not supported")

    @classmethod
    def find_orient(
            cls, solved1, solved2, convert,
            negate=False,
            numPieces=None,
            orientations=None):
        return tuple(cls.find_orientation(
            solved2.permutation[i],
            solved1.permutation[
                convert.permutation[i]],
            negate=negate,
            numPieces=numPieces,
            orientations=orientations)
            for i in range(numPieces))

    @classmethod
    def find_permute(
            cls, solved1, solved2,
            negate=False,
            numPieces=None,
            orientations=None):
        return tuple(
            solved1.permutation.index(
                solved2.permutation[i])
            for i in range(numPieces))

    @classmethod
    def convert(
            cls, orbit_name,
            solved1, solved2,
            coNegate=False,
            moNegate=False,
            numPieces=None,
            orientations=None):
        negate = False
        if coNegate and orbit_name[0:2] == 'CO':
            negate = True
        if moNegate and orbit_name[0:2] == 'CE':
            negate = True

        permutation = cls.find_permute(
            solved1, solved2,
            negate=negate,
            numPieces=numPieces,
            orientations=orientations)
        convert = Orbit.from_dict(dict(
            permutation=permutation,
            orientation=None),
            numPieces=numPieces)
        orientation = cls.find_orient(
            solved1, solved2, convert,
            negate=negate,
            numPieces=numPieces,
            orientations=orientations)

        return Orbit(
            permutation=permutation,
            orientation=orientation)

    @classmethod
    def convert_trans(
            cls, trans_cls, solved1, solved2,
            coNegate=False,
            moNegate=False,
            orbits=None):
        return trans_cls.from_dict(dict([
            (oname,
             cls.convert(
                 oname,
                 getattr(solved1, oname),
                 getattr(solved2, oname),
                 coNegate=coNegate,
                 moNegate=moNegate,
                 numPieces=orbit['numPieces'],
                 orientations=orbit['orientations']))
            for oname, orbit in orbits.items()]))

    def match(self, solv, patt):
        for act, sol, pat in zip(
                self.permutation,
                solv.permutation,
                patt.permutation):
            if pat == 0 and act != sol:
                return False
        for act, sol, pat in zip(
                self.orientation,
                solv.orientation,
                patt.orientation):
            if pat == 0 and act != sol:
                return False
        return True

    def match_trans(self, pattern, orbits=None):
        for orbit_name in orbits.keys():
            if not getattr(self, orbit_name).match(
                    getattr(pattern, orbit_name)):
                return False
        return True
