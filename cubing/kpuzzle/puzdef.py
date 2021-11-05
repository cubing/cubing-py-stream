import os.path
import yaml
from collections import namedtuple
from ..ksolve import (
    puzdef as ksolve_puzdef)


# KPuzzle calls this "PuzzleDefinition"
BasePuzDef = namedtuple('PuzDef', [
    'orbits',
    'moves',
    'startPieces',
    'solvedString'])


class PuzDef(BasePuzDef):

    def __getstate__(self):
        return self._asdict()

    @classmethod
    def from_dict(cls, d):
        if 'startPieces' not in d:
            d['startPieces'] = None
        if 'solvedString' not in d:
            d['solvedString'] = None
        return cls(**d)

    @classmethod
    def from_ksolve(cls, filename):
        if '/' not in filename:
            cls.ksolve_filename = os.path.join(
                os.path.dirname(
                    os.path.dirname(__file__)),
                'puzzles', filename)
        with open(cls.ksolve_filename) as reader:
            return PuzDef.from_reader(reader)

    @classmethod
    def from_kpuzzle(cls, filename):
        if '/' not in filename:
            cls.ksolve_filename = os.path.join(
                os.path.dirname(
                    os.path.dirname(__file__)),
                'puzzles', filename)
        with open(cls.ksolve_filename) as reader:
            d = yaml.safe_load(reader)
            return PuzDef.from_dict(d)

    @classmethod
    def from_reader(cls, reader):
        results = ksolve_puzdef.parse_reader(reader)
        result = ksolve_puzdef.merge_results(results)
        return cls.from_dict(result)

    def to_ksolve(self, nocenter=False):
        rv = ""
        for orbit_name, orbit_def in self.orbits.items():
            rv += ' '.join(["Set", orbit_name,
                            str(orbit_def["numPieces"]),
                            str(orbit_def["orientations"])])
            rv += '\n'
        rv += '\n'

        for move_name, move_def in sorted(self.moves.items()):
            from ..ksolve.reflow import ksolve_script
            rv += ksolve_script(
                move_def,
                header="Move",
                header_name=move_name,
                nocenter=nocenter)
            rv += '\n\n'
        return rv
