
class DisplayMixin:

    def to_display(self):
        # TODO: This requires sticker defs which are
        # outside of the KPUZZLE draft standard.
        # It might be possible to generate this data
        # provided with piece defs, and a general
        # understanding of the sticker layout, but
        # I'm not sure how to do it.
        from ..stickers.stickers_2d import encode
        solved = self.from_dict(self.kpuzzle.startPieces)
        return encode(
            # conjugate solved position
            self.conjugate(solved),
            numSlices=self.num_slices,
            orbitDefs=self.kpuzzle.orbits,
            solvedString=self.kpuzzle.solvedString)

    def display(self):
        print(self.to_display())
        return self
