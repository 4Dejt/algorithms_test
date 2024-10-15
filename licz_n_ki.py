# Dana jest tablica /lista z liczbami naturalnymi.
# Należy policzyć ile jest par elementów o określonym iloczynie.


L = [4,1,5,7,9,4,5,9,6,5,3,2,7,6,1,1,7,9,9,1]

def count_2(t, s, n):
    count = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if t[i] * t[j] == s:
                count += 1
    return count

def count_3(t, s, n):
    count = 0
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j + 1, n):
                if t[i] * t[j] * t[k] == s:
                    count += 1
    return count

x = 0
def count_n_rec(t, s, n, k, p):
    global x
    if k == 1:
        for i in range(p, n):
            if t[i] == s:
                x += 1
    else:
        for i in range(p, n):
            if s % t[i] == 0:
                count_n_rec(t, s//t[i], n, k-1, i+1)


print(count_2(L, 24, len(L)))
print(count_3(L, 24, len(L)))
count_n_rec(L, 24, len(L), 2, 0)
print(x)