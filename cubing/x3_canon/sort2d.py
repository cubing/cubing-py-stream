import json

def tag_facelet(f, centers):
    facelet_tag = (
        int(f[0]) if f[0].isdigit() else 1,
        centers.index(f[1:] if f[0].isdigit() else f))
    return (facelet_tag, f)
    
def tag_cubelet(piece, centers):
    piece2 = list(sorted([
        tag_facelet(facelet, centers=centers)
        for facelet in split_cubelet(piece)
    ]))
    cubelet_tag, piece3 = zip(*piece2) # unzip
    return (cubelet_tag, '_'.join(piece3))

def split_cubelet(piece):
    return piece.split('_') if '_' in piece else list(piece)
    
def sort_orbit(orbit, centers):
    orbit2 = list(sorted([
        tag_cubelet(piece, centers=centers)
        for piece in orbit
    ]))
    _, orbit3 = zip(*orbit2) # unzip
    return orbit3
    
def sort2d(cls, solved, centers, orbit_names):
    return cls.from_dict(dict([
        (orbit_name, {
            'permutation': sort_orbit(getattr(solved, orbit_name).permutation, centers)
        })
        for orbit_name in orbit_names
    ]))
