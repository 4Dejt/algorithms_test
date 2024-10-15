# '0b11010101' = 213

def convert_dec_to_bin(n):
    bin_str = ""
    while n > 0:
        b = n % 2
        n //= 2
        bin_str = str(b) + bin_str
    return bin_str


def convert_dec_to_bin_rec(n):
    if n > 0:
        return convert_dec_to_bin_rec(n // 2) + str(n % 2)
    else:
        return ""




print(convert_dec_to_bin(213))
print(convert_dec_to_bin_rec(213))