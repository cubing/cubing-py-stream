def _get_piece_by_name(piece_name, stickers=None):
    piece = list(stickers[stickers.piece == piece_name]
                 .transpose().to_dict().values())[0]
    return piece


def _get_is_at(piece_num, trans_ori, trans_perm, solved_perm,
               is_active=False, orientations=None, stickers=None):

    # piece_num1 = trans_perm.index(piece_num)
    piece_num2 = trans_perm[piece_num]

    if is_active:
        # Active Permutations
        # Arrays are mappings from Pieces to Spaces
        # Multiplication is p3[i] = p2[p1[i]]

        raise ValueError(
            "Active Permutations should be " +
            "handled primarily by the Orbit class")
    else:
        # Passive Permutations
        # Arrays are mappings from Spaces to Pieces
        # Multiplication is p3[i] = p1[p2[i]]

        # Space (`at`)
        # Has location
        piece_at = _get_piece_by_name(
            solved_perm[piece_num], stickers=stickers)

        # Piece (`is`)
        # Has facelets and orientation
        piece_is = _get_piece_by_name(
            solved_perm[piece_num2], stickers=stickers)
        # piece_is_num = piece_num2

        # Has orientation
        piece_ori = trans_ori[piece_num]

    return [
        (piece_is['piece'][(facelet_num + piece_ori) % orientations],
         int(piece_at['x{}'.format(facelet_num)]),
         int(piece_at['y{}'.format(facelet_num)]))
        for facelet_num in range(orientations)
    ]
