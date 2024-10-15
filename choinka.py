def ch(n, p=0):
    if n == 0:
        pass
    else:
        ch(n-1, p+1)
        print(" " * p, end="")
        print("*" * (2*n -1))

ch(15)