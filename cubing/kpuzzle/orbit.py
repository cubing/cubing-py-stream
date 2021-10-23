from collections import namedtuple

# KPuzzle calls this "Orbit Definition"
BaseOrbitDef = namedtuple('OrbitDef', 'numPieces orientations')

# KPuzzle calls this "Orbit Transformation"
BaseOrbit = namedtuple('Orbit', 'permutation orientation')


# OrbitSequence = list[int]
# OrbitTransformation = tuple[OrbitSequence, OrbitSequence]
# - permutation : OrbitSequence
# - orientation : OrbitSequence
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
        if '_' in name1:
            name1 = tuple(name1.split('_'))
        if '_' in name2:
            name2 = tuple(name2.split('_'))
        # print(repr(name1), repr(name2))
        if tuple(name1) == tuple(name2):
            return 0
        elif orientations == 2:
            if tuple(name1[0:2]) == tuple([name2[1], name2[0]]):
                return 1
            else:
                raise ValueError("Please use eoNegate = True")
        elif orientations == 3:
            if tuple(name1[0:3]) == tuple([name2[1], name2[2], name2[0]]):
                return 1
            elif tuple(name1[0:3]) == tuple([name2[2], name2[0], name2[1]]):
                return 2
            elif tuple(name1[0:3]) == tuple([name2[1], name2[0], name2[2]]) and negate:
                return 2
            elif tuple(name1[0:3]) == tuple([name2[2], name2[1], name2[0]]) and negate:
                return 1
            elif tuple(name1[0:3]) == tuple([name2[0], name2[2], name2[1]]) and negate:
                return 0
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
    def tag_facelet(cls, f, centers=None):
        cfunc = (lambda x: x) if centers is None else centers.index
        facelet_tag = (
            int(f[0]) if f[0].isdigit() else 1,
            cfunc(f[1:] if f[0].isdigit() else f))
        return (facelet_tag, f)
    
    @classmethod
    def tag_cubelet(cls, piece, centers=None):
        piece2 = list(sorted([
            cls.tag_facelet(facelet, centers=centers)
            for facelet in cls.split_cubelet(piece)
        ]))
        cubelet_tag, piece3 = zip(*piece2) # unzip
        return (cubelet_tag, '_'.join(piece3))
    
    @classmethod
    def split_cubelet(cls, piece):
        return piece.split('_') if '_' in piece else list(piece)
    
    @classmethod
    def sort_piece(cls, orbit, centers=None):
        """sort1d"""
        orbit2 = list([
            cls.tag_cubelet(piece, centers=centers)
            for piece in orbit
        ])
        _, orbit3 = zip(*orbit2) # unzip
        return orbit3        

    @classmethod
    def find_permute(
            cls, solved1, solved2,
            negate=False,
            numPieces=None,
            orientations=None):
        perm1 = cls.sort_piece(solved1.permutation)
        perm2 = cls.sort_piece(solved2.permutation)
        return tuple(
            perm1.index(
                perm2[i])
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

    def match_old(self, solv, patt):
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
    
    def match(self, solv):
        """
        This implementation must match
        <https://github.com/Cride5/visualcube/blob/master/cube_lib.php#L964>
        which suppoorts (-1) as a wildcard.

        This implementation shouldn't match
        <https://github.com/cubing/twsearch/blob/main/src/puzdef.h#L102>
        which doesn't support (-1).
        """
        for act, sol in zip(
                self.permutation,
                solv.permutation):
            if act != -1 and sol != -1 and act != sol:
                return False
        for act, sol in zip(
                self.orientation,
                solv.orientation):
            if act != -1 and sol != -1 and act != sol:
                return False
        return True
