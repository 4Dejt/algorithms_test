# a = int(input("podaj a: "))
# b = int(input("podaj b: "))

# rozszerzony algorytm Euklidesa (wersja ze zmiennymi globalnymi)
x = 1
y = 0
def euklides(a, b):
    global x
    global y
    if b != 0:
        euklides(b, a % b);
        x, y = y, x  - a // b * y


euklides(23,13)
print((x,y))
print("-"*20)

# rozszerzony algorytm Euklidesa (wersja rekurencyjna)
def euklides2(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = euklides2(b, a % b)
    return y, x - (a // b) * y, d

print(euklides2(35,14))
