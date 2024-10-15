def is_divisible_by_eleven(n):
    t = abs(sum([int(d) for d in str(n)[::2]]) - sum([int(d) for d in str(n)[1::2]]))
    if n == 0:
        return True
    if n < 10:
        return False
    else:
        return is_divisible_by_eleven(t)


print(is_divisible_by_eleven(121))
print(is_divisible_by_eleven(121*11))

