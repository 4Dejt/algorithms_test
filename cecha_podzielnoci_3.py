def is_divisible_by_three(n):
    total = n
    while True:
        total = sum([int(d) for d in str(total)])
        if total < 10:
            if total in [3, 6, 9]:
                print(f"liczba {n} jest podzielna przez 3")
                break
            else:
                print(f"liczba {n} nie jest podzielna przez 3")
                break

# is_divisible_by_three(3)
# is_divisible_by_three(13)
# is_divisible_by_three(134)
# is_divisible_by_three(1341)
# is_divisible_by_three(1341396)

def is_divisible_by_three_rek(n):
    total = sum([int(d) for d in str(n)])
    if total < 10:
        if total in [3, 6, 9]:
            print(f"liczba jest podzielna przez 3")
        else:
            print(f"liczba jest nie podzielna przez 3")
    else:
        is_divisible_by_three_rek(total)







is_divisible_by_three_rek(3)
is_divisible_by_three_rek(13)
is_divisible_by_three_rek(134)
is_divisible_by_three_rek(1341)
is_divisible_by_three_rek(1341396)