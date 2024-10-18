i = 0

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


fibo(5)
print(i)

# while True:
#     m = int(input("podaj m: "))
#     if m <= 0:
#         break;
#     print(f"fibo({m}) = {fibo(m)}");
