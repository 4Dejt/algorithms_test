def speed_pow(b, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * b
        n = n // 2
        b *= b
    return result

# print(speed_pow(2,0))
def speed_pow_rec(b, n):
    if n == 1:
        return b
    if n % 2 == 0:
        return speed_pow_rec(b, n // 2) * speed_pow_rec(b, n // 2)
    return speed_pow_rec(b, n // 2) * speed_pow_rec(b, n // 2) * b


def speed_pow_rec2(b, n):
    if n == 1:
        return b
    temp = speed_pow_rec(b, n // 2)
    temp = temp * temp
    if n % 2 == 1:
        return b * temp
    return temp



