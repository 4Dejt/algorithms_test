# idea algorytmu:
# 1 warunek bazowy: jeśli mamy permutować zbiór jednoelementowy (lub pusty),
#                   to wynik to po prostu ten zbiór, ponieważ permutacja jednoelementowa
#                   to on sam

# 2 rekursja: Aby wygenerować permutacje dla zbioru o rozmiarze nn:
#               a)      wybierz jeden element ze zbioru;
#               b)      znajdź wszystkie permutacje pozostałych n−1 elementów;
#               c)      wstaw wybrany element na wszystkie możliwe pozycje w każdej
#                       z tych permutacji.


def permutation(s):
    if len(s) == 1:
        return [s]

    result = []
    for i in range(len(s)):
        # wybierz element s[i], pozostałe elementy to s[:i] + s[i+1:]
        rest = s[:i] + s[i + 1:]
        for p in permutation(rest):
            result.append([s[i]] + p)

    return result


# przykład użycia
s = [1, 2, 3]


print(permutation(s))