from unittest import TestCase
from cubing.x3 import Transform as X3


class TestX3TwizzleFormats(TestCase):

    x3_class = X3

    def assert_equal_pos(self, pos1, pos2):
        self.assertEqual(
            pos1.EDGES.permutation,
            pos2.EDGES.permutation)
        self.assertEqual(
            pos1.EDGES.orientation,
            pos2.EDGES.orientation)
        self.assertEqual(
            pos1.CORNERS.permutation,
            pos2.CORNERS.permutation)
        self.assertEqual(
            pos1.CORNERS.orientation,
            pos2.CORNERS.orientation)
        self.assertEqual(
            pos1.CENTERS.permutation,
            pos2.CENTERS.permutation)
        self.assertEqual(
            pos1.CENTERS.orientation,
            pos2.CENTERS.orientation)

    def test_F_kpuzzle(self):
        actual = type(self).x3_class.from_alg("F")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [9, 1, 2, 3, 8, 5, 6, 7, 0, 4, 10, 11],
                "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
            },
            "CORNERS": {
                "permutation": [3, 1, 2, 5, 0, 4, 6, 7],
                "orientation": [1, 0, 0, 2, 2, 1, 0, 0]
            },
            "CENTERS": {
                "permutation": [0, 1, 2, 3, 4, 5],
                "orientation": [0, 0, 1, 0, 0, 0]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_F_reidstr(self):
        actual_s = type(self).x3_class.from_alg("F").to_reidstr()
        expect_s = "LF UR UB UL RF DR DB DL FU FD BR BL " + \
            "LFU URB UBL LDF RUF RFD DLB DBR U L F R B D"
        self.assertEqual(actual_s, expect_s)

    def test_F_stickers(self):
        actual_s = type(self).x3_class.from_alg("F").to_stickers()
        expect_s = [0, 0, 0, 0, 0, 0, 1, 1, 1,
                    1, 1, 5, 1, 1, 5, 1, 1, 5,
                    2, 2, 2, 2, 2, 2, 2, 2, 2,
                    0, 3, 3, 0, 3, 3, 0, 3, 3,
                    4, 4, 4, 4, 4, 4, 4, 4, 4,
                    3, 3, 3, 5, 5, 5, 5, 5, 5]
        self.assertEqual(actual_s, expect_s)

    def test_B(self):
        actual = type(self).x3_class.from_alg("B")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [0, 1, 10, 3, 4, 5, 11, 7, 8, 9, 6, 2],
                "orientation": [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
            },
            "CORNERS": {
                "permutation": [0, 7, 1, 3, 4, 5, 2, 6],
                "orientation": [0, 2, 1, 0, 0, 0, 2, 1]
            },
            "CENTERS": {
                "permutation": [0, 1, 2, 3, 4, 5],
                "orientation": [0, 0, 0, 0, 1, 0]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_D(self):
        actual = type(self).x3_class.from_alg("D")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CORNERS": {
                "permutation": [0, 1, 2, 3, 5, 6, 7, 4],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CENTERS": {
                "permutation": [0, 1, 2, 3, 4, 5],
                "orientation": [0, 0, 0, 0, 0, 1]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_U(self):
        actual = type(self).x3_class.from_alg("U")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CORNERS": {
                "permutation": [1, 2, 3, 0, 4, 5, 6, 7],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CENTERS": {
                "permutation": [0, 1, 2, 3, 4, 5],
                "orientation": [1, 0, 0, 0, 0, 0]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_L(self):
        actual = type(self).x3_class.from_alg("L")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [0, 1, 2, 11, 4, 5, 6, 9, 8, 3, 10, 7],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CORNERS": {
                "permutation": [0, 1, 6, 2, 4, 3, 5, 7],
                "orientation": [0, 0, 2, 1, 0, 2, 1, 0]
            },
            "CENTERS": {
                "permutation": [0, 1, 2, 3, 4, 5],
                "orientation": [0, 1, 0, 0, 0, 0]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_R(self):
        actual = type(self).x3_class.from_alg("R")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [0, 8, 2, 3, 4, 10, 6, 7, 5, 9, 1, 11],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CORNERS": {
                "permutation": [4, 0, 2, 3, 7, 5, 6, 1],
                "orientation": [2, 1, 0, 0, 1, 0, 0, 2]
            },
            "CENTERS": {
                "permutation": [0, 1, 2, 3, 4, 5],
                "orientation": [0, 0, 0, 1, 0, 0]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_M(self):
        actual = type(self).x3_class.from_alg("M")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [2, 1, 6, 3, 0, 5, 4, 7, 8, 9, 10, 11],
                "orientation": [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
            },
            "CORNERS": {
                "permutation": [0, 1, 2, 3, 4, 5, 6, 7],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CENTERS": {
                "permutation": [4, 1, 0, 3, 5, 2],
                "orientation": [2, 0, 0, 0, 2, 0]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_E(self):
        actual = type(self).x3_class.from_alg("E")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 8, 10],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
            },
            "CORNERS": {
                "permutation": [0, 1, 2, 3, 4, 5, 6, 7],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CENTERS": {
                "permutation": [0, 4, 1, 2, 3, 5],
                "orientation": [0, 0, 0, 0, 0, 0]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_S(self):
        actual = type(self).x3_class.from_alg("S")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [0, 3, 2, 7, 4, 1, 6, 5, 8, 9, 10, 11],
                "orientation": [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]
            },
            "CORNERS": {
                "permutation": [0, 1, 2, 3, 4, 5, 6, 7],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CENTERS": {
                "permutation": [1, 5, 2, 0, 4, 3],
                "orientation": [1, 1, 0, 1, 0, 1]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_x(self):
        actual = type(self).x3_class.from_alg("x")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [4, 8, 0, 9, 6, 10, 2, 11, 5, 7, 1, 3],
                "orientation": [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
            },
            "CORNERS": {
                "permutation": [4, 0, 3, 5, 7, 6, 2, 1],
                "orientation": [2, 1, 2, 1, 1, 2, 1, 2]
            },
            "CENTERS": {
                "permutation": [2, 1, 5, 3, 0, 4],
                "orientation": [0, 3, 0, 1, 2, 2]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_y(self):
        actual = type(self).x3_class.from_alg("y")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [1, 2, 3, 0, 5, 6, 7, 4, 10, 8, 11, 9],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
            },
            "CORNERS": {
                "permutation": [1, 2, 3, 0, 7, 4, 5, 6],
                "orientation": [0, 0, 0, 0, 0, 0, 0, 0]
            },
            "CENTERS": {
                "permutation": [0, 2, 3, 4, 1, 5],
                "orientation": [1, 0, 0, 0, 0, 3]
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_z(self):
        actual = type(self).x3_class.from_alg("z")
        expect = type(self).x3_class.from_dict({
            "EDGES": {
                "permutation": [9, 3, 11, 7, 8, 1, 10, 5, 0, 4, 2, 6],
                "orientation": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            },
            "CORNERS": {
                "permutation": [3, 2, 6, 5, 0, 4, 7, 1],
                "orientation": [1, 2, 1, 2, 2, 1, 2, 1]
            },
            "CENTERS": {
                "permutation": [1, 5, 2, 0, 4, 3],
                "orientation": [1, 1, 1, 1, 3, 1]
            }
        })
        self.assert_equal_pos(actual, expect)
