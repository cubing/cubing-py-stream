from cubing.kpuzzle.puzgeo import (dump_moves)
from cubing.x3 import Transform as X3


normalVectors = {
    "U": (0, 1, 0),
    "L": (-1,  0, 0),
    "F": (0, 0, 1),
    "R": (1, 0, 0),
    "B": (0, 0, -1),
    "D": (0, -1, 0),
}

solvedString = {
  "EDGES": {
    "permutation": [
        "UL", "UF", "UR", "UB",
        "BL", "FL", "FR", "BR",
        "DL", "DF", "DR", "DB"],
    "orientation": [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0]
  },
  "CORNERS": {
    "permutation": [
        "UBL", "ULF", "UFR", "URB",
        "DLB", "DFL", "DRF", "DBR"],
    "orientation": [
        0, 0, 0, 0,
        0, 0, 0, 0]
  },
  "CENTERS": {
    "permutation": [
        "U", "L", "F", "R", "B", "D"],
    "orientation": [
        0, 0, 0, 0, 0, 0]
  }
}

moves = "U L F R B D".split(" ")

def main():
    dump_moves(
        X3, moves,
        numTwists=4,
        normalVectors=normalVectors,
        solvedString=solvedString,
        shortForm=True)
  
if __name__ == '__main__':
    main()
