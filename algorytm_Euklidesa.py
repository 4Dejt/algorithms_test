# algorytm Euklidesa wersja iteracyjna (odejmowanie)
def nwd1(a,b):
    while b != a:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# algorytm Euklidesa wersja iteracyjna (dzielenie)
def nwd2(a,b):
    while a > 0:
        r = b % a
        a, b = r, a

    return b

# algorytm Euklidesa wersja rekurencyjna (odejmowanie)
def nwd1_rec(a,b):
    if a == b:
        return a
    elif a > b:
        return  nwd1_rec(a - b, b)
    else:
        return nwd1_rec(a, b - a)

# algorytm Euklidesa wersja rekurencyjna (dzielenie)
def nwd2_rec(a,b):
    if b == 0:
        return a
    else:
        return nwd2_rec(b, b % a)

a = int(input("podaj a: "))
b = int(input("podaj b: "))
print(f"nwd({a}, {b}) = {nwd2_rec(a,b)}")
