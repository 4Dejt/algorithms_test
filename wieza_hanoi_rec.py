from time import sleep

# wersja z listami
def tower_hanoi_1(n, A, B, C):
    if n > 0:
        tower_hanoi_1(n-1, A, C, B)
        C.append(A.pop())
        print(f"===================")
        print(A)
        print(B)
        print(C)
        print(f"===================")
        sleep(2)
        tower_hanoi_1(n-1, B, A, C)

# n = int(input("podaj liczbę krążków: "))
# A = [i for i in range(n, 0, -1)]
# B = []
# C = []
# tower_hanoi_1(n, A, B, C)

def tower_hanoi_2(n, from_, using_, to_):
    if n > 0:
        tower_hanoi_2(n-1, from_, to_, using_)
        print(f"{from_}-->{to_}")
        tower_hanoi_2(n-1, using_, from_, to_)

tower_hanoi_2(3,"A","B","C")