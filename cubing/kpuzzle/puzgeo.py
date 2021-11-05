
import numpy
import pandas
from collections.abc import Sequence
from numpy import (cos, sin)

def split_piece(piece, shortForm=False):
    return list(piece) if shortForm else piece.split("_")

def build_piece(piece, shortForm=False):
    return "".join(piece) if shortForm else "_".join(piece)

def average(xs):
    z = (0, 0, 0)
    for x in xs:
        z = numpy.array([
            z[0] + x[0],
            z[1] + x[1],
            z[2] + x[2]])
    return z

def rotate(th, ux, uy, uz):
    rot_mat = numpy.array([
        [cos(th) + ux**2*(1 - cos(th)),
         ux*uy*(1 - cos(th)) - uz*sin(th),
         ux*uz*(1 - cos(th)) + uy*sin(th)],
        [uy*ux*(1 - cos(th)) + uz*sin(th),
         cos(th) + uy**2*(1 - cos(th)),
         uy*uz*(1 - cos(th)) - ux*sin(th)],
        [uz*ux*(1 - cos(th)) - uy*sin(th),
         uz*uy*(1 - cos(th)) + ux*sin(th),
         cos(th) + uz**2*(1 - cos(th))]])
    return rot_mat

def pieces_in_layer(cls, move, orbit, solvedString, shortForm=False):
    return set([
        piece
        for piece in solvedString[orbit]['permutation']
        if move in split_piece(piece, shortForm=shortForm)
    ])

def piece_coords(cls, piece, orbit, normalVectors, shortForm=False):
    if orbit[0:2] == 'CO':
        nfacelets = 3
    elif orbit[0:2] == 'ED':
        nfacelets = 2
    elif orbit[0:2] == 'CE':
        nfacelets = 1
    else:
        raise ValueError

    facelets = split_piece(piece, shortForm=shortForm)
    # print(repr(piece), repr(facelets))
    vpiece = average([
        normalVectors[facelets[f]]
        for f in range(nfacelets)])
    vfacelets = [
        average([
            vpiece,
            normalVectors[facelets[f]]])
        for f in range(nfacelets)]
    return dict([
        ('_ID', piece),
        (piece, vpiece)] + [
            (facelets[f], vfacelets[f])
            for f in range(nfacelets)])
        
def match_vec(vec1, vec2, epsilon=0.001):
    if isinstance(vec1, (str, bytes)):
        return False
    if not isinstance(vec1, (Sequence, numpy.ndarray)):
        return False
    if not isinstance(vec2, (Sequence, numpy.ndarray)):
        return False
#     print(repr(vec1), repr(vec2))
    vec3 = numpy.array(vec1) - numpy.array(vec2)
    if (vec3[0]**2 + vec3[1]**2 + vec3[2]**2) < epsilon:
        return True
    return False

def match_piece(cls, space_vec, coords2s):
    return list(set([
        k
        for coord in coords2s
        for k, v in coord.items()
        if match_vec(v, space_vec)]))

def match_piece_ori(cls, space_vec, coords2s):
    return list(set([
        (k, coord['_ID'])
        for coord in coords2s
        for k, v in coord.items()
        if match_vec(v, space_vec)]))

def find_perm(cls, move, numTwists, normalVectors, orbitDefs, solvedString, shortForm=False):
    results = dict()
    for orbit in orbitDefs.keys():
        if orbit in ['CENTERS']:
            continue
        if orbit not in results:
            results[orbit] = dict()
        coords1s = {}
        coords2s = []
        
        for piece in list(pieces_in_layer(
                cls, move, orbit,
                solvedString=solvedString,
                shortForm=shortForm)):
            coords1 = piece_coords(
                cls, piece, orbit,
                normalVectors=normalVectors,
                shortForm=shortForm)
            # print(repr(coords1))
            coords1s[piece] = coords1[piece]
            degrees = float(360.0)/float(numTwists)
            mat = rotate(float(degrees)/180.0*numpy.pi, *normalVectors[move])
            coords2 = dict([
                (key, mat @ numpy.array(coords1[key]))
                if not key.startswith("_") else (key, coords1[key])
                for key in coords1.keys()])
            coords2s.append(coords2)
        
        for piece in list(pieces_in_layer(
                cls, move, orbit,
                solvedString=solvedString,
                shortForm=shortForm)):
            piece_vec = coords1s[piece]
            spaces = match_piece(cls, piece_vec, coords2s)
            if len(spaces) == 1:
                space = spaces[0]
                results[orbit][space] = piece
            else:
                print("invalid results", repr(spaces))
    return results

def find_orientation(
        cls, name1, name2,
        negate=False,
        numPieces=None,
        orientations=None):
    if name1.startswith('_'):
        print("BAD START")
        return -1
    if name2.startswith('_'):
        print("BAD START")
        return -1
    if '_' in name1:
        name1 = tuple(name1.split('_'))
    if '_' in name2:
        name2 = tuple(name2.split('_'))
    if len(name1) != len(name2):
        print("BAD LEN")
        return -1
    if tuple(name1) == tuple(name2):
        return 0
    elif orientations == 2:
        if tuple(name1[0:2]) == tuple([name2[1], name2[0]]):
            return 1
        else:
            raise ValueError("Please use eoNegate = True")
    elif orientations == 3:
        if tuple(name1[0:3]) == tuple([name2[1], name2[2], name2[0]]):
            return 2
        elif tuple(name1[0:3]) == tuple([name2[2], name2[0], name2[1]]):
            return 1
        elif tuple(name1[0:3]) == tuple([name2[1], name2[0], name2[2]]) and negate:
            return 2
        elif tuple(name1[0:3]) == tuple([name2[2], name2[1], name2[0]]) and negate:
            return 1
        elif tuple(name1[0:3]) == tuple([name2[0], name2[2], name2[1]]) and negate:
            return 0
        else:
            raise ValueError("Please use coNegate = True")
    else:
        raise ValueError("corners not supported")

def find_ori(cls, move, numTwists, normalVectors, orbitDefs, solvedString, shortForm=False):
    results = {}
    for orbit in orbitDefs.keys():
        if orbit in ['CENTERS']:
            continue
        coords1s = {}
        coords2s = []
        results[orbit] = {}
        orientations = 1
        if orbit[0:2] == 'ED':
            orientations = 2
        elif orbit[0:2] == 'CO':
            orientations = 3
        
        for piece in list(pieces_in_layer(
                cls, move, orbit,
                solvedString=solvedString,
                shortForm=shortForm)):
            coords1 = piece_coords(
                cls, piece, orbit,
                normalVectors=normalVectors,
                shortForm=shortForm)
            for facelet in split_piece(piece, shortForm=shortForm):
                coords1s[piece + "_" + facelet] = coords1[facelet]
            degrees = float(360.0)/float(numTwists)
            mat = rotate(float(degrees)/180.0*numpy.pi, *normalVectors[move])
            coords2 = dict([
                (key, mat @ numpy.array(coords1[key]))
                if not key.startswith("_") else (key, coords1[key])
                for key in coords1.keys()])
            coords2s.append(coords2)

        for piece in list(pieces_in_layer(
                cls, move, orbit,
                solvedString=solvedString,
                shortForm=shortForm)):
            spaces = sum([
                match_piece_ori(cls, coords1s[piece + "_" + facelet], coords2s)
                for facelet in split_piece(piece, shortForm=shortForm)
            ], [])
            try:
                spaces2, spaces3 = zip(*spaces)  # unzip
            except:
                # print(repr(piece))
                continue
            spaces3 = list(set(spaces3))[0]
            results[orbit][spaces3] = {
                "facelets": spaces2,
                "piece_name": spaces3,
                "space_name": piece,
                "orients": find_orientation(
                    cls, spaces3,
                    build_piece(spaces2, shortForm=shortForm),
                    orientations=orientations)
            }
    return results

def build_trans(cls, move, numTwists, normalVectors, solvedString, orbitDefs, shortForm):
    t = cls.new()
    perm_results = find_perm(
        cls, move,
        numTwists=numTwists,
        normalVectors=normalVectors,
        orbitDefs=orbitDefs,
        solvedString=solvedString,
        shortForm=shortForm)
    ori_results = find_ori(
        cls, move,
        numTwists=numTwists,
        normalVectors=normalVectors,
        orbitDefs=orbitDefs,
        solvedString=solvedString,
        shortForm=shortForm)
    for orbit in orbitDefs.keys():
        if orbit in ['CENTERS']:
            continue
        npieces = orbitDefs[orbit]['numPieces']
        solved = solvedString[orbit]['permutation']
        
        # permutation
        p = [i for i in range(npieces)]
        for k, v in perm_results[orbit].items():
            p[solved.index(k)] = solved.index(v)

        # orientation
        o = [0 for i in range(npieces)]
        for k, v in ori_results[orbit].items():
            o[solved.index(v['space_name'])] = v['orients']
            
        # transformation
        t = t._replace(**dict([(orbit, getattr(t, orbit)._replace(
            permutation=p, 
            orientation=o))]))
        
    for orbit in ['CENTERS']:
        npieces = orbitDefs[orbit]['numPieces']
        solved = solvedString[orbit]['permutation']
        # orientation
        o = [0 for i in range(npieces)]
        o[solved.index(move)] = 1
        # transformation
        t = t._replace(**dict([(orbit, getattr(t, orbit)._replace(
            orientation=o))]))
        
    return t


def dump_moves(
        cls, moves,
        numTwists,
        normalVectors,
        solvedString,
        shortForm=False):
    for move in moves:
        print()
        build_trans(
            cls, move,
            numTwists=numTwists,
            normalVectors=normalVectors,
            solvedString=solvedString,
            shortForm=shortForm,
            orbitDefs=cls.kpuzzle.orbits
        ).ksolve("Move", move, nocenter=False)
    
