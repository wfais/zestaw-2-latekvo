def depth(x):
    if isinstance(x, list):
        return 1 + (max([depth(e) for e in x]) if x else 0)
    if isinstance(x, tuple):
        return 1 + (max([depth(e) for e in x]) if x else 0)
    if isinstance(x, dict):
        return 1 + (max([depth(v) for v in x.values()]) if x else 0)
    return 0

def apply(x, d, max_d):
    if isinstance(x, list):
        if d == max_d:
            x.append(len(x)+1)
        for e in x:
            apply(e, d+1, max_d)
    elif isinstance(x, tuple):
        for e in x:
            apply(e, d+1, max_d)
    elif isinstance(x, dict):
        for v in x.values():
            apply(v, d+1, max_d)

def dodaj_element(wejscie):
    max_d = depth(wejscie)
    apply(wejscie, 1, max_d)
    return wejscie

if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)   
