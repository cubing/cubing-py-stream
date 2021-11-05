from . import (
    orbit as ksolve_orbit)


def do_set_cmd(line, result, lines):
    _, name, size, ori = line.split(' ')
    if 'orbits' not in result:
        result['orbits'] = {}
    if name not in result['orbits']:
        result['orbits'][name] = {
            "numPieces": int(size),
            "orientations": int(ori),
        }


def parse_line(line, result, lines):
    line = line.strip()
    if len(line) == 0:
        return
    elif line.startswith("#"):
        return
    elif line.startswith("Name"):
        return
    elif line.startswith("Set"):
        do_set_cmd(line, result, lines)
    elif line == "Solved":
        if "solved" not in result:
            result["solved"] = {}
    elif line == "SolvedString":
        if "solvedString" not in result:
            result["solvedString"] = {}
    elif line == "Ignore":
        if "ignored" not in result:
            result["ignored"] = {}
    elif line.startswith("IgnoreSet"):
        _, name = line.split(' ')
        name = name.strip()
        if "ignoreSets" not in result:
            result["ignoreSets"] = {}
        if name not in result["ignoreSets"]:
            result["ignoreSets"][name] = {}
    elif line.startswith("Scramble"):
        _, name = line.split(' ')
        name = name.strip()
        if "scrambles" not in result:
            result["scrambles"] = {}
        if name not in result["scrambles"]:
            result["scrambles"][name] = {}
    elif line.startswith("Move"):
        _, name = line.split(' ')
        name = name.strip()
        if "moves" not in result:
            result["moves"] = {}
        if name not in result["moves"]:
            result["moves"][name] = {}
    elif line == "End":
        if not len(result.keys()):
            raise ValueError("no result")
        cmd = list(result.keys())[0]
        if cmd == "moves":
            ksolve_orbit.do_named_cmd("moves", result, lines)
        elif cmd == "scrambles":
            ksolve_orbit.do_named_cmd("scrambles", result, lines)
        elif cmd == "solved":
            ksolve_orbit.do_simple_cmd("solved", result, lines)
        elif cmd == "solvedString":
            ksolve_orbit.do_simple_cmd("solvedString", result, lines)
    else:
        lines.append(line)


def parse_reader(reader):
    results = []
    last_lines = []
    last_result = dict()
    for line in reader.readlines():
        parse_line(line, last_result, last_lines)
        if line.startswith('End') or \
           line.startswith('Set') or \
           line.startswith('Name'):
            results.append(last_result)
            last_lines = []
            last_result = dict()
    return results


def merge_results(results):
    result = {}
    result['orbits'] = {}
    result['moves'] = {}

    for r in results:
        if 'solved' in r:
            result['startPieces'] = r['solved']
        if 'solvedString' in r:
            result['solvedString'] = r['solvedString']
        if 'orbits' in r:
            result['orbits'].update(r['orbits'])
        if 'moves' in r:
            result['moves'].update(r['moves'])

    if 'solvedString' not in result:
        result['solvedString'] = None

    if 'solvedstartPieces' in result:
        result["startPieces"] = None
    return result
