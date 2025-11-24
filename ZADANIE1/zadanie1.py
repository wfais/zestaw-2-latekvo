def dodaj_element(wejscie):
    def max_depth(x):
        if isinstance(x, list):
            return 1 + (max([max_depth(e) for e in x]) if x else 0)
        if isinstance(x, tuple):
            return 1 + (max([max_depth(e) for e in x]) if x else 0)
        if isinstance(x, dict):
            return 1 + (max([max_depth(v) for v in x.values()]) if x else 0)
        return 0

    target = max_depth(wejscie)

    deepest_lists = []

    def collect(x, depth):
        if isinstance(x, list):
            if depth == target:
                deepest_lists.append(x)
            for e in x:
                collect(e, depth + 1)
        elif isinstance(x, tuple):
            for e in x:
                collect(e, depth + 1)
        elif isinstance(x, dict):
            for v in x.values():
                collect(v, depth + 1)

    collect(wejscie, 1)

    for lst in deepest_lists:
        if lst:
            mx = max(e for e in lst if isinstance(e, (int, float)))
            lst.append(mx + 1)
        else:
            lst.append(1)

    return wejscie

