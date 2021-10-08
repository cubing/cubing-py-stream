def json_reflow(s):
    """
    Not much more than json.dumps(). This function
    takes a string with newlines between each
    element of a list, and compresses it to be
    a one-line list. For example:

    '''
    [a,
     b,
     c]
    '''

    becomes: [a, b, c]. Pretty simple.
    """
    import re
    matches = re.findall(r'\[[\"\'A-Za-z0-9,\s\n]+\]', s)
    for match in matches:
        # print(type(match))
        repl = re.sub(r'\n\s+', ' ', match)
        repl = re.sub(r'\[ ', '[', repl)
        repl = re.sub(r' \]', ']', repl)
        s = s.replace(match, repl)
    return s


def ksolve_reflow(d):
    try:
        return dict([
            (orbit_name, dict(
                permutation=[i + 1 for i in orbit_trans["permutation"]],
                orientation=[i for i in orbit_trans["orientation"]]))
            for orbit_name, orbit_trans in d.items()
        ])
    except TypeError:
        return dict([
            (orbit_name, dict(
                permutation=[i for i in orbit_trans["permutation"]],
                orientation=[i for i in orbit_trans["orientation"]]))
            for orbit_name, orbit_trans in d.items()
        ])


def ksolve_script(d, header="Move", header_name="A",
                  footer="End", nocenter=True):
    if header in ["Solved", "SolvedString"]:
        header_name = ""
    if header != "SolvedString":
        d = ksolve_reflow(d)
    middle = ""
    for orbit_name, orbit_trans in reversed(sorted(
            d.items(), key=lambda x: x[0])):
        if nocenter and orbit_name.startswith("CE"):
            continue
        if not orbit_trans['orientation']:
            middle += orbit_name + '\n'
            middle += ' '.join(map(str, orbit_trans['permutation'])) + '\n'
        elif not all([isinstance(v, int) for v in orbit_trans['permutation']]):
            middle += orbit_name + '\n'
            middle += ' '.join(map(str, orbit_trans['permutation'])) + '\n'
        elif any([v - k - 1 for k, v in enumerate(
                orbit_trans['permutation'])]) or any(
                orbit_trans['orientation']):
            middle += orbit_name + '\n'
            middle += ' '.join(map(str, orbit_trans['permutation'])) + '\n'
            if any(orbit_trans['orientation']):
                middle += ' '.join(map(str, orbit_trans['orientation'])) + '\n'
        elif any(orbit_trans['orientation']):
            middle += orbit_name + '\n'
            middle += ' '.join(map(str, orbit_trans['permutation'])) + '\n'
            middle += ' '.join(map(str, orbit_trans['orientation'])) + '\n'
    return """{header} {header_name}\n{middle}{footer}""".format(
        header_name=header_name,
        header=header,
        middle=middle,
        footer=footer)
