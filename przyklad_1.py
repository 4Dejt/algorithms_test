i = 0

def find(x, left, right, array):
    global i
    i += 1
    print(f"Wywolanie nr {i}")
    if left > right:
        print(f"Element {x} nie zostal znaleziony w tablicy!")
    elif x == array[left]:
        print(f"Element {x} zostal znaleziony w tablicy na pozycji {left}!")
    else:
        find(x, left + 1, right, array);
    i -= 1
    print(f"Koniec wywolania nr {i}");



t=[2,-3,5,8,10,11,0,-33,12,14]

print("-----------PRZYKLAD 1------------")
find(5, 0, len(t)-1, t)
print("-----------PRZYKLAD 2------------")
find(12, 0, len(t)-1, t)
print("-----------PRZYKLAD 3------------")
find(77, 0, len(t)-1, t)
