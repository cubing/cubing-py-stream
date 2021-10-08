
def parse_numbers(*plines):
    pline = plines[0]
    ps = pline.split(' ')
    ps = [p for p in ps if p]
    if len(ps) and not ps[0].isdigit():
        ps = ' '.join(plines).split(' ')
        ps = [p for p in ps if p]
        return {
            "permutation": ps,
            "orientation": None}
    else:
        ps = [int(p) - 1 for p in ps]
        if not len(plines[1:]):
            os = [0 for _ in range(len(ps))]
        else:
            oline = plines[1]
            os = oline.split(' ')
            os = [int(o) for o in os]
        return {
            "permutation": ps,
            "orientation": os}


def parse_orbits(result, lines):
    liness = [[]]
    for line in lines:
        if len(line) and ' ' in line:
            liness[-1].append(line)
        else:
            liness.append([])
            liness[-1].append(line)
    for group in liness:
        if len(group) == 0:
            continue
        elif len(group) == 3:
            orbit = group[0].strip()
            result[orbit] = parse_numbers(group[1], group[2])
        elif len(group) == 2:
            orbit = group[0].strip()
            result[orbit] = parse_numbers(group[1])
        else:
            orbit = group[0].strip()
            result[orbit] = parse_numbers(*group[1:])
        # raise ValueError("unknown orbit")


def do_simple_cmd(result_name, result, lines):
    parse_orbits(result[result_name], lines)


def do_named_cmd(result_name, result, lines):
    name = list(result[result_name].keys())[0]
    parse_orbits(result[result_name][name], lines)
