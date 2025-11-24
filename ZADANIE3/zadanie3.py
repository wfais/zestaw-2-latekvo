import requests, re, time, sys
from collections import Counter

URL = "https://pl.wikipedia.org/api/rest_v1/page/random/summary"
N = 100 
HEADERS = {
    "User-Agent": "wp-edu-wiki-stats/0.1 (kontakt: ignacy.latka@student.uj.edu.pl)",
    "Accept": "application/json",
}

WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)

def selekcja(text: str):
    words = WORD_RE.findall(text or "")
    res = [w.lower() for w in words if len(w) > 3]
    return res


def ramka(text: str, width: int = 80) -> str:
    if width < 3:
        raise ValueError("width musi być co najmniej 3")
    content_width = width - 2
    s = text or ""
    if len(s) > content_width:
        s = s[: content_width - 1] + "…"
    centered = s.center(content_width)
    return f"[{centered}]"


def main():
    cnt = Counter()
    licznik_slow = 0
    pobrane = 0

    # linia statusu
    print(ramka("Start"), end="", flush=True)

    while pobrane < N:
        try:
            data = requests.get(URL, headers=HEADERS, timeout=10).json()
        except Exception:
            time.sleep(0.1)
            continue

        title = data.get("title") or ""
        line = "\r" + ramka(title, 80)
        print(line, end="", flush=True)

        extract = data.get("extract") or ""
        lista = selekcja(extract)
        cnt.update(lista)
        licznik_slow += len(lista)
        pobrane += 1
        time.sleep(0.05)

    print()

    print(f"Pobrano: {pobrane}")
    print(f"#Słowa:  {licznik_slow}")
    print(f"Unikalne:  {len(cnt)}\n")

    print("Najczęstsze 15 słów:")
    for word, count in cnt.most_common(15):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()

