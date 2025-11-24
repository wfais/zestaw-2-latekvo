roman_map = {
    'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
}

valid_subtractive = {
    'I':('V','X'),
    'X':('L','C'),
    'C':('D','M')
}

def rzymskie_na_arabskie(rzymskie):
    if not isinstance(rzymskie, str):
        raise TypeError("Oczekiwano str.")

    if not rzymskie or any(ch not in roman_map for ch in rzymskie):
        raise ValueError("Niepoprawne symbole rzymskie.")

    total = 0
    i = 0
    while i < len(rzymskie):
        v = roman_map[rzymskie[i]]
        if i+1 < len(rzymskie):
            n = roman_map[rzymskie[i+1]]
            if n > v:
                if rzymskie[i] not in valid_subtractive or rzymskie[i+1] not in valid_subtractive[rzymskie[i]]:
                    raise ValueError("Niepoprawny zapis rzymski.")
                total += n - v
                i += 2
                continue
        total += v
        i += 1

    if not (1 <= total <= 3999) or arabskie_na_rzymskie(total) != rzymskie:
        raise ValueError("Niepoprawny zapis rzymski.")
    return total


def arabskie_na_rzymskie(arabskie):
    if not isinstance(arabskie, int):
        raise TypeError("Oczekiwano int.")
    if not (1 <= arabskie <= 3999):
        raise ValueError("Liczba musi być w zakresie 1-3999.")

    symbols = [
        (1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
        (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
        (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')
    ]

    res = []
    n = arabskie
    for v,s in symbols:
        q, n = divmod(n, v)
        if q:
            res.append(s*q)
        if n == 0:
            break
    return ''.join(res)


if __name__ == '__main__':
    try:
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
    except ValueError as e:
        print(e)

