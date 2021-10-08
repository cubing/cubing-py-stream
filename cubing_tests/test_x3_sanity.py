from unittest import TestCase
from cubing.x3 import Transform as X3


class TestX3Sanity(TestCase):

    x3_class = X3

    def assert_equal_trans(self, pos1, pos2, msg=None):
        self.assertEqual(
            pos1.EDGES.permutation,
            pos2.EDGES.permutation,
            msg=msg)
        self.assertEqual(
            pos1.EDGES.orientation,
            pos2.EDGES.orientation,
            msg=msg)
        self.assertEqual(
            pos1.CORNERS.permutation,
            pos2.CORNERS.permutation,
            msg=msg)
        self.assertEqual(
            pos1.CORNERS.orientation,
            pos2.CORNERS.orientation,
            msg=msg)
        self.assertEqual(
            pos1.CENTERS.permutation,
            pos2.CENTERS.permutation,
            msg=msg)
        self.assertEqual(
            pos1.CENTERS.orientation,
            pos2.CENTERS.orientation,
            msg=msg)

    moves_to_test = "ULFRBDMESxyz"

    def test_moves(self):
        for move in list(type(self).moves_to_test):
            msg = "Move {}".format(move)
            self.assertTrue(move in type(self).x3_class.move_defs, msg=msg)

    def test_display(self):
        expect_s = "\n".join([
            "   UDU      ",
            "   DUD      ",
            "   UDU      ",
            "LRLFBFRLRBFB",
            "RLRBFBLRLFBF",
            "LRLFBFRLRBFB",
            "   DUD      ",
            "   UDU      ",
            "   DUD      "])
        actual_t = type(self).x3_class.from_alg("M2 E2 S2")
        self.assertEqual(actual_t.to_display(), expect_s)
