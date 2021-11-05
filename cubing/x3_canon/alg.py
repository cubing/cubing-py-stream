import re
from .grip import Grip
from .move import Move
from ..x3 import Transform as Pos3
from .constants import (
    NOTATIONS, UNHANDINGS,
    COLLATIONS, OPTIMIZATIONS)


'''

Definition of Unhanding (Hand-2-Face):

1. Group Expansion
   - Replace `(R U)3` with `R U R U R U`. Getting rid
     of groups allows us to assume they don't exist.
2. Notation Substitution
   - Replace `Rw` with `r` and so on. There are many
     common notation systems with identical symantics.     
3. Notation Expansion
   - Replace `r` with `x' L'`, `M` with `x' L' R", and so on.
     This makes the unhanding step easier.
4. Rotation Deletion (Unhanding)
   - To get rid of rotations, we need substitution tables
     for all possible rotations. This is easily created
     by the position class (Pos) using get_rotation().

Definition of Canonicalization (requires Unhanding):

5. Parallel Compression
   - It is common while mining to encounter sequences
     of steps like `L R L R L R` which is equivalent to
     `L' R'`, but require advanced recognition.
6. Parallel Collation
   - It is common to see parallel moves written either
     `L R` or `R L`, and in this step we enforce that they
     are written in alphabetical order, which implies
     that both are written `L R`. The other sides are
     ordered `B F` not `F B`, and `D U` not `U D`.
7. Optimization
   - It is common while mining to encounter sequences
     of steps like `L2 R2 B2 F2 L2 R2 B2 F2` which are
     no-ops but can appear to be doing something.

Definition of Adjusted-Canonicalization:

8a. Adjust Upper Face for First Two Layers (AUF-F2L)
    - Generally done with `U` moves before the algorithm.
8b. Adjust Upper Face to Orient Last Layer Adjust Upper Face (AUF-OLL)
    - Generally done with `y` moves before the algorithm.
    - Must be one of the 8 Birdflu orientations.
8c. Adjust Upper Face to Permute Last Layer Adjust Upper Face (AUF-PLL)
    - Generally done with `y` moves before the algorithm.
    - Diagonal corner swaps must be between B and D.
    - Adjacent corner swaps must be between C and D.
9. Return the algorithm if found in the database.
'''


class Unhander(object):
    
    def __init__(self):
        self.pos = Pos3.new()
        self.alg = ''

    def try_unhanding(self, step):
        if step == 'moves':
            return None
        try:
            rp = self.pos.CENTERS.permutation
            step2 = Grip.faces[rp[
                Grip.faces.index(step[0])]]
            if step.endswith("'"):
                step2 += "'"
            elif step.endswith("2"):
                step2 += "2"
            return step2
        except Exception as exc:
            # print(repr(exc), repr(step))
            raise
    
    def do_turn(self, step):
        if not len(step):
            return
        
        if step[0] not in Grip.dims:
            step = self.try_unhanding(step)
            if step is None: return
            self.alg += ' ' + str(step)
            self.alg = self.alg.strip()
            
        self.pos = self.pos.alg(step)

    @classmethod
    def unhand(cls, alg):
        """
        """
        unhander = cls()
        for step in alg.split(' '):
            unhander.do_turn(step)
        # print(repr(vars(unhander)))
        return unhander.alg.strip()

_repetition_re = re.compile(
    r"\((?P<alg>[\w\s\']+)\)(?P<num>\d)")
_non_group_re = re.compile(
    r"[^\w\s\']")
def _expand_repetition(alg_code):
    while True:
        match = _repetition_re.search(alg_code)
        if not match:
            break
        repnum = match.group('num')
        repnum = int(repnum)
        subalg = match.group('alg')
        subalg += " "
        alg_code = alg_code.replace(match.group(0), subalg*repnum)
    alg_code = _non_group_re.sub('', alg_code)
    alg_code = alg_code.strip()
    return alg_code


def _expand_notations(alg):
    alg += ' '
    for d in NOTATIONS.transpose().to_dict().values():
        alg = alg.replace(d['pattern'] + " ", d['replace'] + " ")
    return alg


def _expand_unhanding(alg):
    alg += ' '
    for d in UNHANDINGS.transpose().to_dict().values():
        alg = alg.replace(d['pattern'] + " ", d['replace'] + " ")
    return alg.strip()


def expand(alg, unhanding=False):
    alg += ' '
    alg = _expand_repetition(alg) 
    alg = _expand_notations(alg)
    if unhanding:
        alg = _expand_unhanding(alg)
    return alg.strip()



def _dump_move(move, amount):
    if amount == 3:
        return "{}'".format(move)
    elif amount == 2:
        return "{}2".format(move)
    else:
        return move
    
def _parse_move(move):
    if move.endswith("'"):
        return (move[0], 3)
    elif move.endswith("2"):
        return (move[0], 2)
    else:
        return (move, 1)

def _sum_moves(moves, ntwists=4):
    # This is what enforces alphabetical order
    keys = sorted(list(set([
        move[0] for move in moves
    ])))
    return [
        (key, sum([
            move[1]
            for move in moves
            if move[0] == key
        ]) % ntwists)
        for key in keys
    ]

def _parallel_collate1(alg, ntwists=4):
    parts = alg.split(' ')
    parts2 = []
    cur_dim = None
    for move in parts:
        if not len(move):
            continue
        dim = Grip.get_layer(move[0]).dim
        if cur_dim != dim:
            cur_dim = dim
            parts2.append([])
        parts2[-1].append(move)
        
    # group L's and R's together
    parts3 = list(map(sorted, parts2))

    # add up each group
    parts4 = [
        _sum_moves([
            # (name, amount)
            _parse_move(move)
            for move in moves
        ], ntwists=4)
        for moves in parts3
    ]
    
    # filter out empty move's
    parts5 = [
        [
            (move, amount)
            for move, amount in moves
            if amount != 0
        ]
        for moves in parts4
    ]
    
    # filter out empty moves's
    parts6 = [
        moves
        for moves in parts5
        if len(moves) > 0
    ]
    parts7 = sum(parts6, [])
    parts8 = list(map(lambda x: _dump_move(x[0], x[1]), parts7))
    return ' '.join(parts8)


def _cummutes_with(move, move2):
    if move == move2:
        return True
    elif move == "R" and move2 == "L":
        return True
    elif move == "L" and move2 == "R":
        return True
    elif move == "F" and move2 == "B":
        return True
    elif move == "B" and move2 == "F":
        return True
    elif move == "D" and move2 == "U":
        return True
    elif move == "U" and move2 == "D":
        return True
    else:
        return False
    
def _cummutes_with_all(move, moves):
    return all([
        _cummutes_with(move, move2)
        for move2 in moves])

def _get_cummutes(family):
    if   family in "LR": return "LR"
    elif family in "BF": return "BF"
    elif family in "DU": return "DU"
    else: raise ValueError

def _commutes_build(moves_out, commutes_dict):
    for family, amount in sorted(commutes_dict.items()):
        if amount == 0:
            continue
        moves_out.append(Move(family, amount))

        
def _parallel_collate(alg, ntwists=4):
    moves = map(Move, alg.strip().split(' '))
    moves_out = []
    
    commutes_dict = {}
    for move in moves:
        
        # check if commutes_dict is empty
        if move.family not in commutes_dict.keys():
            commutes_dict[move.family] = 0

        if not _cummutes_with_all(move.family, commutes_dict.keys()):
            # switch to new dimension
            # convert commutes_dict to moves_out
            _commutes_build(moves_out, commutes_dict)
            commutes_dict = {}

        # append to current dimension
        # combine move amounts from nearby moves
        if move.family not in commutes_dict.keys():
            commutes_dict[move.family] = 0
        commutes_dict[move.family] += move.amount
        commutes_dict[move.family] %= ntwists

    # switch to new dimension
    # convert commutes_dict to moves_out
    _commutes_build(moves_out, commutes_dict)
    s = ' '.join(list(map(str, moves_out)))
    if s == alg.strip():
        return s
    else:
        return _parallel_collate(s)
        
        

def _parallel_optimize(alg):
    for d in OPTIMIZATIONS.transpose().to_dict().values():
        alg = alg.replace(d['pattern'] + ' ', d['replace'] + ' ')
    return alg

def optimize(alg):
    """
    """
    alg += ' '
    alg = _parallel_collate(alg)
    alg = _parallel_optimize(alg)
    return alg.strip()


def canonicalize1(alg):
    """
    """
    alg = expand(alg, unhanding=True)
    alg = optimize(Unhander.unhand(alg))
    alg = expand(alg, unhanding=False)
    return alg


def canonicalize(alg, oob=False):
    if not oob:
        return canonicalize1(alg)
    for prefix, postfix in [("", ""), ("y", "y'"), ("y2", "y2"), ("y'", "y")]:
        a = "{} {} {}".format(prefix, alg, postfix)
        b = canonicalize1(a)
        if not b:
            continue
        bi = b.index(" ") + 1
        if b[0] == 'B':
            return b
        if b[0] == 'D' and b[bi] == 'B':
            return b
    else:
        return None
