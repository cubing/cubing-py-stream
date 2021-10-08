
class X3FormatsMixin:

    @classmethod
    def from_birdf2l_id(cls, birdf2l_id):
        from .birdf2l import decode
        return decode(cls, birdf2l_id)

    def to_birdf2l_id(self):
        from .birdf2l import encode
        return encode(type(self), self)

    @classmethod
    def from_birdflu_id(cls, birdflu_id):
        from .birdflu_ll_pos import decode
        return decode(cls, birdflu_id)

    def to_birdflu_id(self):
        from .birdflu_ll_pos import encode
        return encode(type(self), self)

    @classmethod
    def from_birdflu_code(cls, birdflu_id):
        from .birdflu_ll_code import decode
        return decode(cls, birdflu_id)

    def to_birdflu_code(self):
        from .birdflu_ll_code import encode
        return encode(type(self), self)

    @classmethod
    def from_binary(cls, binary_id):
        from .binary import decode
        return decode(cls, binary_id)

    def to_binary(self, mo=False):
        from .binary import encode
        return encode(type(self), self, mo=mo)

    @classmethod
    def from_binary_d(cls, binary_d):
        from .binary import _decode_d
        return _decode_d(cls, binary_d)

    def to_binary_d(self, mo=False):
        from .binary import _encode_d
        return _encode_d(type(self), self, mo=mo)

    @classmethod
    def from_reidstr(cls, s):
        from ..stickers.reid_str import decode
        return decode(cls, s)

    def to_reidstr(self):
        from ..stickers.reid_str import encode
        solved = self.from_dict(self.kpuzzle.startPieces)
        return encode(
            type(self),
            self.conjugate(solved),
            numSlices=self.num_slices,
            orbitDefs=self.kpuzzle.orbits,
            solvedString=self.kpuzzle.solvedString)

    @classmethod
    def from_stickers(cls, stickers):
        from ..stickers.stickers_1d import decode
        return decode(cls, stickers)

    def to_stickers(self):
        from ..stickers.stickers_1d import encode
        solved = self.from_dict(self.kpuzzle.startPieces)
        return encode(
            type(self),
            self.conjugate(solved),
            numSlices=self.num_slices,
            orbitDefs=self.kpuzzle.orbits,
            solvedString=self.kpuzzle.solvedString)

    def respect(self):
        from ..x3_speffz import TO_SPEFFZ_D
        r2speffz = type(self).from_dict(TO_SPEFFZ_D)
        return self.conjugate(r2speffz)

    def disrespect(self):
        from ..x3_speffz import TO_SPEFFZ_D
        speffz2r = type(self).from_dict(TO_SPEFFZ_D).__neg__()
        return self.conjugate(speffz2r)

    @classmethod
    def init_x3(cls2, cls):

        # outer block moves on the 3x3x3
        cls.move_defs["Uw"] = cls.from_alg("U E'").__getstate__()
        cls.move_defs["Lw"] = cls.from_alg("L M").__getstate__()
        cls.move_defs["Fw"] = cls.from_alg("F S").__getstate__()
        cls.move_defs["Rw"] = cls.from_alg("R M'").__getstate__()
        cls.move_defs["Bw"] = cls.from_alg("B S'").__getstate__()
        cls.move_defs["Dw"] = cls.from_alg("D E").__getstate__()
        cls.move_defs["u"] = cls.from_alg("U E'").__getstate__()
        cls.move_defs["l"] = cls.from_alg("L M").__getstate__()
        cls.move_defs["f"] = cls.from_alg("F S").__getstate__()
        cls.move_defs["r"] = cls.from_alg("R M'").__getstate__()
        cls.move_defs["b"] = cls.from_alg("B S'").__getstate__()
        cls.move_defs["d"] = cls.from_alg("D E").__getstate__()
        cls.init_moves()
