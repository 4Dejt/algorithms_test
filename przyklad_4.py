def factorial(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f;


   
m = int(input("podaj m: "))
print(f"{m}! = {factorial(m)}");
