
print("Hola Mundo")

def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


x = int(input("ingrese numero: "))
fib(x)
