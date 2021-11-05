from cubing.kpuzzle.puzgeo import (dump_moves)
from cubing.megaminx import Transform as MM


# Constants
c1 = 0.276393038153934 # z
c2 = 0.447213915054917 # y
c3 = 0.52573110541762  # x
c4 = 0.723606953208851 # z
c5 = 0.850650812993204 # x
c6 = 0.894427031222365 # z

normalVectors = {
    "U": (0, 1, 0),
    "BL": (-c3, c2, -c4),
    "L": (-c5, c2, c1),
    "F": (0, c2, c6),
    "R": (c5, c2, c1),
    "BR": (c3, c2, -c4),
    "DL": (-c5, -c2, -c1),
    "FL": (-c3, -c2, c4),
    "FR": (c3, -c2, c4),
    "DR": (c5, -c2, -c1),
    "B": (0, -c2, -c6),
    "D": (0, -1, 0),
}

solvedString = {
    "EDGES": {
        "permutation": [
            "U_BL", "U_L", "U_F", "U_R", "U_BR",
            "BL_L", "L_F", "F_R", "R_BR", "BR_BL",
            "BL_B", "BL_DL", "L_DL", "L_FL", "F_FL",
            "F_FR", "R_FR", "R_DR", "BR_DR", "BR_B",
            "B_DL", "DL_FL", "FL_FR", "FR_DR", "DR_B",
            "D_DL", "D_FL", "D_FR", "D_DR", "D_B"],
        "orientation": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    },
    "CORNERS": {
        "permutation": [
            "U_BL_L", "U_L_F", "U_F_R", "U_R_BR", "U_BR_BL",
            "DL_L_BL", "FL_F_L", "FR_R_F", "DR_BR_R", "B_BL_BR",
            "BL_B_DL", "L_DL_FL", "F_FL_FR", "R_FR_DR", "BR_DR_B",
            "D_DL_B", "D_FL_DL", "D_FR_FL", "D_DR_FR", "D_B_DR"],
        "orientation": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    },
    "CENTERS": {
        "permutation": [
            "U", "BL", "L", "F", "R", "BR",
            "DL", "FL", "FR", "DR", "B", "D"],
        "orientation": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
}

moves = "U BL L F R BR DL FL FR DR B D".split(" ")

def main():
    dump_moves(
        MM, moves,
        numTwists=5,
        normalVectors=normalVectors,
        solvedString=solvedString,
        shortForm=False)
  
if __name__ == '__main__':
    main()
