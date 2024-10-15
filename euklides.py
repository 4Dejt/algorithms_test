def euklides(a,b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

print(euklides(44, 11))

def euklides_extended(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print(euklides_extended(44, 11))