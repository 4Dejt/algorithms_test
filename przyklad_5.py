def fibo(n):
    f1, f2 = 1, 1
    for i in range(n-1):
        f1, f2 = f2, f1 + f2
    return f1



while True:
    m = int(input("podaj m: "))
    if m <= 0:
        break
    print(f"fibo({m}) = {fibo(m)}");

