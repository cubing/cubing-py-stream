import pandas


NOTATIONS = pandas.DataFrame([
    {
        "pattern": "'2",
        "replace": "2"
    },
    {
        "pattern": "2'",
        "replace": "2"
    },
    {
        "pattern": "Ri",
        "replace": "R'"
    },
    {
        "pattern": "Ui",
        "replace": "U'"
    },
    {
        "pattern": "Fi",
        "replace": "F'"
    },
    {
        "pattern": "Li",
        "replace": "L'"
    },
    {
        "pattern": "Di",
        "replace": "D'"
    },
    {
        "pattern": "Bi",
        "replace": "B'"
    },
    {
        "pattern": "r",
        "replace": "Rw"
    },
    {
        "pattern": "r2",
        "replace": "Rw2"
    },
    {
        "pattern": "r'",
        "replace": "Rw'"
    },
    {
        "pattern": "u",
        "replace": "Uw"
    },
    {
        "pattern": "u2",
        "replace": "Uw2"
    },
    {
        "pattern": "u'",
        "replace": "Uw'"
    },
    {
        "pattern": "f",
        "replace": "Fw"
    },
    {
        "pattern": "f2",
        "replace": "Fw2"
    },
    {
        "pattern": "f'",
        "replace": "Fw'"
    },
    {
        "pattern": "l",
        "replace": "Lw"
    },
    {
        "pattern": "l2",
        "replace": "Lw2"
    },
    {
        "pattern": "l'",
        "replace": "Lw'"
    },
    {
        "pattern": "d",
        "replace": "Dw"
    },
    {
        "pattern": "d2",
        "replace": "Dw2"
    },
    {
        "pattern": "d'",
        "replace": "Dw'"
    },
    {
        "pattern": "b",
        "replace": "Bw"
    },
    {
        "pattern": "b2",
        "replace": "Bw2"
    },
    {
        "pattern": "b'",
        "replace": "Bw'"
    },
    {
        "pattern": "[r']",
        "replace": "x'"
    },
    {
        "pattern": "[r2]",
        "replace": "x2"
    },
    {
        "pattern": "[r]",
        "replace": "x"
    },
    {
        "pattern": "[u']",
        "replace": "y'"
    },
    {
        "pattern": "[u2]",
        "replace": "y2"
    },
    {
        "pattern": "[u]",
        "replace": "y"
    },
    {
        "pattern": "[f']",
        "replace": "z'"
    },
    {
        "pattern": "[f2]",
        "replace": "z2"
    },
    {
        "pattern": "[f]",
        "replace": "z"
    }
])

UNHANDINGS = pandas.DataFrame([
    {
        "pattern": "M",
        "replace": "x' L' R"
    },
    {
        "pattern": "M2",
        "replace": "x2 L2 R2"
    },
    {
        "pattern": "M'",
        "replace": "x L R'"
    },
    {
        "pattern": "E",
        "replace": "y' D' U"
    },
    {
        "pattern": "E2",
        "replace": "y2 D2 U2"
    },
    {
        "pattern": "E'",
        "replace": "y D U'"
    },
    {
        "pattern": "S'",
        "replace": "z' B' F"
    },
    {
        "pattern": "S2",
        "replace": "z2 B2 F2"
    },
    {
        "pattern": "S",
        "replace": "z B F'"
    },
    {
        "pattern": "Lw",
        "replace": "x' R"
    },
    {
        "pattern": "Lw2",
        "replace": "x2 R2"
    },
    {
        "pattern": "Lw'",
        "replace": "x R'"
    },
    {
        "pattern": "Rw",
        "replace": "x L"
    },
    {
        "pattern": "Rw2",
        "replace": "x2 L2"
    },
    {
        "pattern": "Rw'",
        "replace": "x' L'"
    },
    {
        "pattern": "Uw",
        "replace": "y D"
    },
    {
        "pattern": "Uw2",
        "replace": "y2 D2"
    },
    {
        "pattern": "Uw'",
        "replace": "y' D'"
    },
    {
        "pattern": "Dw",
        "replace": "y' U"
    },
    {
        "pattern": "Dw2",
        "replace": "y2 U2"
    },
    {
        "pattern": "Dw'",
        "replace": "y U'"
    },
    {
        "pattern": "Fw",
        "replace": "z B"
    },
    {
        "pattern": "Fw2",
        "replace": "z2 B2"
    },
    {
        "pattern": "Fw'",
        "replace": "z' B'"
    },
    {
        "pattern": "Bw",
        "replace": "z' F"
    },
    {
        "pattern": "Bw2",
        "replace": "z2 F2"
    },
    {
        "pattern": "Bw'",
        "replace": "z F'"
    }
])


COLLATIONS = pandas.DataFrame([
    {
        "pattern": "R L",
        "replace": "L R"
    },
    {
        "pattern": "R L2",
        "replace": "L2 R"
    },
    {
        "pattern": "R L'",
        "replace": "L' R"
    },
    {
        "pattern": "R2 L",
        "replace": "L R2"
    },
    {
        "pattern": "R2 L2",
        "replace": "L2 R2"
    },
    {
        "pattern": "R2 L'",
        "replace": "L' R2"
    },
    {
        "pattern": "R' L",
        "replace": "L R'"
    },
    {
        "pattern": "R' L2",
        "replace": "L2 R'"
    },
    {
        "pattern": "R' L'",
        "replace": "L' R'"
    },
    {
        "pattern": "F B",
        "replace": "B F"
    },
    {
        "pattern": "F B2",
        "replace": "B2 F"
    },
    {
        "pattern": "F B'",
        "replace": "B' F"
    },
    {
        "pattern": "F2 B",
        "replace": "B F2"
    },
    {
        "pattern": "F2 B2",
        "replace": "B2 F2"
    },
    {
        "pattern": "F2 B'",
        "replace": "B' F2"
    },
    {
        "pattern": "F' B",
        "replace": "B F'"
    },
    {
        "pattern": "F' B2",
        "replace": "B2 F'"
    },
    {
        "pattern": "F' B'",
        "replace": "B' F'"
    },
    {
        "pattern": "U D",
        "replace": "D U"
    },
    {
        "pattern": "U D2",
        "replace": "D2 U"
    },
    {
        "pattern": "U D'",
        "replace": "D' U"
    },
    {
        "pattern": "U2 D",
        "replace": "D U2"
    },
    {
        "pattern": "U2 D2",
        "replace": "D2 U2"
    },
    {
        "pattern": "U2 D'",
        "replace": "D' U2"
    },
    {
        "pattern": "U' D",
        "replace": "D U'"
    },
    {
        "pattern": "U' D2",
        "replace": "D2 U'"
    },
    {
        "pattern": "U' D'",
        "replace": "D' U'"
    }
])

OPTIMIZATIONS = pandas.DataFrame([
    {
        "pattern": "B2 F2 L2 R2 B2 F2",
        "replace": "L2 R2"
    },
    {
        "pattern": "D2 U2 L2 R2 D2 U2",
        "replace": "L2 R2"
    },
    {
        "pattern": "B2 F2 D2 U2 B2 F2",
        "replace": "D2 U2"
    },
    {
        "pattern": "L2 R2 D2 U2 L2 R2",
        "replace": "D2 U2"
    },
    {
        "pattern": "L2 R2 B2 F2 L2 R2",
        "replace": "B2 F2"
    },
    {
        "pattern": "D2 U2 B2 F2 D2 U2",
        "replace": "B2 F2"
    },
    {
        "pattern": "L2 R D2 U2 L2 R2 D2",
        "replace": "R'"
    },
    {
        "pattern": "B2 F L2 R2 B2 F2 L2",
        "replace": "F' R2"
    },
    {
        "pattern": "L2 R' B2 F2 L2 R2 B2 F",
        "replace": "R F'"
    }
])
