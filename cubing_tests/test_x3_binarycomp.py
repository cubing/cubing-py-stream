from unittest import TestCase
from cubing.x3 import Transform as X3


class TestX3TwizzleBinaryComponents(TestCase):

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

    def assert_equal_dict(self, d1, d2):
        t1 = tuple(sorted(d1.items()))
        t2 = tuple(sorted(d2.items()))
        self.assertEqual(t1, t2)

    # F

    def test_F_decode_ctr(self):
        binary_d = {
            "epLex": 363310128,
            "eoMask": 2188,
            "cpLex": 16008,
            "coMask": 2412,
            "poIdxU": 0,
            "poIdxL": 0,
            "moSupport": 1,
            "moMask": 64
        }
        actual = type(self).x3_class.from_binary_d(binary_d)
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
                "orientation": [0, 0, 1, 0, 0, 0]  # notice the one
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_F_decode_noc(self):
        binary_d = {
            "epLex": 363310128,
            "eoMask": 2188,
            "cpLex": 16008,
            "coMask": 2412,
            "poIdxU": 7,
            "poIdxL": 0,
            "moSupport": 0,
            "moMask": 0
        }
        actual = type(self).x3_class.from_binary_d(binary_d)
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
                "orientation": [0, 0, 0, 0, 0, 0]  # notice the zero
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_F_encode_ctr(self):
        binary_d = {
            "epLex": 363310128,
            "eoMask": 2188,
            "cpLex": 16008,
            "coMask": 2412,
            "poIdxU": 0,
            "poIdxL": 0,
            "moSupport": 1,
            "moMask": 64
        }
        actual = type(self).x3_class.from_alg("F").to_binary_d(mo=True)
        self.assert_equal_dict(actual, binary_d)

    def test_F_encode_noc(self):
        binary_d = {
            "epLex": 363310128,
            "eoMask": 2188,
            "cpLex": 16008,
            "coMask": 2412,
            "poIdxU": 7,
            "poIdxL": 0,
            "moSupport": 0,
            "moMask": 0
        }
        actual = type(self).x3_class.from_alg("F").to_binary_d(mo=False)
        self.assert_equal_dict(actual, binary_d)

    # R

    def test_R_decode_ctr(self):
        binary_d = {
            "epLex": 25813736,
            "eoMask": 0,
            "cpLex": 20325,
            "coMask": 5132,
            "poIdxU": 0,
            "poIdxL": 0,
            "moSupport": 1,
            "moMask": 16
        }
        actual = type(self).x3_class.from_binary_d(binary_d)
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
                "orientation": [0, 0, 0, 1, 0, 0]  # notice the one
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_R_decode_noc(self):
        binary_d = {
            "epLex": 25813736,
            "eoMask": 0,
            "cpLex": 20325,
            "coMask": 5132,
            "poIdxU": 7,
            "poIdxL": 0,
            "moSupport": 0,
            "moMask": 0
        }
        actual = type(self).x3_class.from_binary_d(binary_d)
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
                "orientation": [0, 0, 0, 0, 0, 0]  # notice the zero
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_R_encode_ctr(self):
        binary_d = {
            "epLex": 25813736,
            "eoMask": 0,
            "cpLex": 20325,
            "coMask": 5132,
            "poIdxU": 0,
            "poIdxL": 0,
            "moSupport": 1,
            "moMask": 16
        }
        actual = type(self).x3_class.from_alg("R").to_binary_d(mo=True)
        self.assertEqual(actual, binary_d)

    def test_R_encode_noc(self):
        binary_d = {
            "epLex": 25813736,
            "eoMask": 0,
            "cpLex": 20325,
            "coMask": 5132,
            "poIdxU": 7,
            "poIdxL": 0,
            "moSupport": 0,
            "moMask": 0
        }
        actual = type(self).x3_class.from_alg("R").to_binary_d(mo=False)
        self.assertEqual(actual, binary_d)

    # U

    def test_U_decode_ctr(self):
        binary_d = "14 ef ec 00 00 0b 7c 00 00 14 00"
        actual = type(self).x3_class.from_binary(binary_d)
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
                "orientation": [1, 0, 0, 0, 0, 0]  # notice the one
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_U_decode_noc(self):
        binary_d = "14 ef ec 00 00 0b 7c 00 03 80 00"
        actual = type(self).x3_class.from_binary(binary_d)
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
                "orientation": [0, 0, 0, 0, 0, 0]  # notice the zero
            }
        })
        self.assert_equal_pos(actual, expect)

    def test_U_encode_ctr(self):
        binary_d = "14 ef ec 00 00 0b 7c 00 00 14 00"
        actual = type(self).x3_class.from_alg("U").to_binary(mo=True)
        self.assertEqual(actual, binary_d)

    def test_U_encode_noc(self):
        binary_d = "14 ef ec 00 00 0b 7c 00 03 80 00"
        actual = type(self).x3_class.from_alg("U").to_binary(mo=False)
        self.assertEqual(actual, binary_d)

    # Birdflu F1

    def test_F1_encode_ctr(self):
        binary_d = "03 75 f0 03 00 0a 14 12 fc 10 00"
        actual = type(self).x3_class.from_alg(
            "R B U B' U' R'").to_binary(mo=True)
        self.assertEqual(actual, binary_d)

    def test_F1_encode_noc(self):
        binary_d = "03 75 f0 03 00 0a 14 12 ff 80 00"
        actual = type(self).x3_class.from_alg(
            "R B U B' U' R'").to_binary(mo=False)
        self.assertEqual(actual, binary_d)

    # Birdflu F2

    def test_F2_encode_ctr(self):
        binary_d = "16 aa e4 02 80 0a 14 12 fc 10 00"
        actual = type(self).x3_class.from_alg(
            "L U F U' F' L'").to_binary(mo=True)
        self.assertEqual(actual, binary_d)

    def test_F2_encode_noc(self):
        binary_d = "16 aa e4 02 80 0a 14 12 ff 80 00"
        actual = type(self).x3_class.from_alg(
            "L U F U' F' L'").to_binary(mo=False)
        self.assertEqual(actual, binary_d)

    # Birdflu F3

    def test_F3_encode_ctr(self):
        binary_d = "01 e7 44 01 80 0a 14 12 fc 10 00"
        actual = type(self).x3_class.from_alg(
            "L' B' U' B U L").to_binary(mo=True)
        self.assertEqual(actual, binary_d)

    def test_F3_encode_noc(self):
        binary_d = "01 e7 44 01 80 0a 14 12 ff 80 00"
        actual = type(self).x3_class.from_alg(
            "L' B' U' B U L").to_binary(mo=False)
        self.assertEqual(actual, binary_d)

    # Birdflu F4

    def test_F4_encode_ctr(self):
        binary_d = "39 46 44 02 80 0a 14 12 fc 10 00"
        actual = type(self).x3_class.from_alg(
            "R' U' F' U F R").to_binary(mo=True)
        self.assertEqual(actual, binary_d)

    def test_F4_encode_noc(self):
        binary_d = "39 46 44 02 80 0a 14 12 ff 80 00"
        actual = type(self).x3_class.from_alg(
            "R' U' F' U F R").to_binary(mo=False)
        self.assertEqual(actual, binary_d)
