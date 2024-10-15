def print_digits(n):
    while n > 0:
        print(n % 10)
        n //= 10


def print_digits_rec_1(n):
    if n > 0:
        print(n % 10)
        print_digits_rec_1(n//10)


def print_digits_rec_2(n):
    if n > 0:
        print_digits_rec_2(n//10)
        print(n % 10)

print_digits(2135)
print("-" * 12)
print_digits_rec_1(2135)
print("-" * 12)
print_digits_rec_2(2135)