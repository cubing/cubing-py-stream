from unittest import TestCase
from cubing.x3 import Transform as X3
from cubing.x3_formats.birdflu_ll_pos import decode, encode
from cubing.x3_speffz import TO_SPEFFZ_D


class TestX3BirdfluPositionIdentifier(TestCase):

    x3_class = X3
    r2s_trans = X3.from_dict(TO_SPEFFZ_D)

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

    # Birdflu F1

    def test_F1_decode(self):
        alg = "R B U B' U' R' U"
        ll_pos = 'Dd1i'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_F1_encode(self):
        alg = "R B U B' U' R' U"
        ll_pos = 'Dd1i'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu F2

    def test_F2_decode(self):
        alg = "L U F U' F' L' U"
        ll_pos = 'Dd6j'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_F2_encode(self):
        alg = "L U F U' F' L' U"
        ll_pos = 'Dd6j'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu F3

    def test_F3_decode(self):
        alg = "L' B' U' B U L U"
        ll_pos = 'Dd1f'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_F3_encode(self):
        alg = "L' B' U' B U L U"
        ll_pos = 'Dd1f'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu F4

    def test_F4_decode(self):
        alg = "R' U' F' U F R U"
        ll_pos = 'Dd9e'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_F4_encode(self):
        alg = "R' U' F' U F R U"
        ll_pos = 'Dd9e'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G1 - Wide-Sune

    def test_G1_decode(self):
        alg = "B L F' L F L2 B' U2"
        ll_pos = 'Bo6F'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G1_encode(self):
        alg = "B L F' L F L2 B' U2"
        ll_pos = 'Bo6F'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G2 - Anti-Wide-Sune

    def test_G2_decode(self):
        alg = "F R2 B' R' B R' F' U2"
        ll_pos = 'bo9E'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G2_encode(self):
        alg = "F R2 B' R' B R' F' U2"
        ll_pos = 'bo9E'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G3 - Sune

    def test_G3_decode(self):
        alg = "F U F' U F U2 F' U2"
        ll_pos = 'Bo4E'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G3_encode(self):
        alg = "F U F' U F U2 F' U2"
        ll_pos = 'Bo4E'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G4 - Niklas

    def test_G4_decode(self):
        alg = "F U' B' U F' U' B U"
        ll_pos = 'Bb4A'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G4_encode(self):
        alg = "F U' B' U F' U' B U"
        ll_pos = 'Bb4A'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G5 - Anti-Sune

    def test_G5_decode(self):
        alg = "B U2 B' U' B U' B' U2"
        ll_pos = 'bo4F'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G5_encode(self):
        alg = "B U2 B' U' B U' B' U2"
        ll_pos = 'bo4F'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G6 - Left-Wide-Sune

    def test_G6_decode(self):
        alg = "L' B' R B' R' B2 L U2"
        ll_pos = 'bo8K'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G6_encode(self):
        alg = "L' B' R B' R' B2 L U2"
        ll_pos = 'bo8K'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G7 - Anti-Left-Wide-Sune

    def test_G7_decode(self):
        alg = "R' F2 L F L' F R U2"
        ll_pos = 'Bo9L'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G7_encode(self):
        alg = "R' F2 L F L' F R U2"
        ll_pos = 'Bo9L'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G8 - Left-Niklas

    def test_G8_decode(self):
        alg = "R' U L U' R U L' U'"
        ll_pos = 'bl4A'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G8_encode(self):
        alg = "R' U L U' R U L' U'"
        ll_pos = 'bl4A'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G9 - Left-Sune

    def test_G9_decode(self):
        alg = "R' U' R U' R' U2 R U2"
        ll_pos = 'bo4L'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G9_encode(self):
        alg = "R' U' R U' R' U2 R U2"
        ll_pos = 'bo4L'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu G10 - Anti-Left-Sune

    def test_G10_decode(self):
        alg = "L' U2 L U L' U L U2"
        ll_pos = 'Bo4K'

        expect_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual_t = decode(type(self).x3_class, ll_pos)
        self.assert_equal_pos(actual_t, expect_t)

    def test_G10_encode(self):
        alg = "L' U2 L U L' U L U2"
        ll_pos = 'Bo4K'

        actual_t = type(self).x3_class.\
            from_alg(alg).conjugate(
                type(self).r2s_trans).__neg__()

        actual = encode(type(self).x3_class, actual_t)
        self.assertEqual(actual, ll_pos)

    # Birdflu H1
