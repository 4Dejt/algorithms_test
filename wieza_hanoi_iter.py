from time import sleep
n = int(input("podaj liczbę krążków: "))
A = [i for i in range(n, 0, -1)]
B = []
C = []
j = 0
small = True
while len(B) < n and len(C) < n:
    j += 1
    if small:
        if A and A[-1] == 1:
            x = A.pop()
            if not B or B[-1] > x:
                B.append(x)
            else:
                C.append(x)
        elif B and B[-1] == 1:
            x = B.pop()
            if not C or C[-1] > x:
                C.append(x)
            else:
                A.append(x)
        else:
            x = C.pop()
            if not A or A[-1] > x:
                A.append(x)
            else:
                B.append(x)
        small = False
    else:
        if A and A[-1] != 1 and (not B or A[-1] < B[-1]):
            x = A.pop()
            B.append(x)
        elif A and A[-1] != 1 and (not C or A[-1] < C[-1]):
            x = A.pop()
            C.append(x)
        elif B and B[-1] != 1 and (not C or B[-1] < C[-1]):
            x = B.pop()
            C.append(x)
        elif B and B[-1] != 1 and (not A or B[-1] < A[-1]):
            x = B.pop()
            A.append(x)
        elif C and C[-1] != 1 and (not A or C[-1] < A[-1]):
            x = C.pop()
            A.append(x)
        else:
            x = C.pop()
            B.append(x)
        small = True
    print(f"========={j}=========")
    print(A)
    print(B)
    print(C)
    print(f"===================")
    sleep(2)







