from unittest import TestCase
from cubing.x5 import Transform as X5


class TestX5Sanity(TestCase):

    x5_class = X5

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

    moves_to_test = "B,2B,S,2F,F,D,2D,E,2U,U,L,2L,M,2R,R,x,y,z".split(",")

    def test_moves(self):
        for move in type(self).moves_to_test:
            msg = "Move {}".format(move)
            self.assertTrue(move in type(self).x5_class.move_defs, msg=msg)
