# suma 1 + 2 + 3 + ... + n
def s1(n):
    if n == 0:
        return 0
    else:
        return n + s1(n-1)

# suma cyfr liczby
def s2(n):
    if n == 0:
        return 0
    else:
        return n % 10 + s2(n//10)

print(s1(20))
print(s2(564))