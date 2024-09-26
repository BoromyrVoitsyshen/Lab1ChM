import math

#функція для методу простої ітерації
def phi(x):
    return 1 + (5 * math.sin(x) - 1) / (x**2) + x

#функція для методу релаксації
def f(x):
    return x**2 + 5 * math.sin(x) - 1

#цикл для методу релаксації
def relax(a, b, N, m1, M1, eps):
    x = (a + b) / 2
    t = 2 / (m1 + M1)
    prevX = x
    for i in range(1, N + 1):
        prevX = x
        x = x + t * f(x)
        print(x, x-prevX)

#цикл для методу простої ітерації
def simpleIter(a, b, N, eps):
    x = (a + b) / 2
    for i in range(1, N + 1):
        prevX = x
        x = phi(x)
        print(x, x-prevX)

#обираємо проміжок та вказуємо точність
a = -3
b = -2
N = 15
eps = 0.0001

#вказуємо необхідні значення для методу релаксації
m1 = 11
M1 = 6
#проходимо цикл методу простої ітерації
print("SimpleIter")
simpleIter(a, b, N, eps)
#проходимо цикл методу релаксації
print("Relax")
relax(a, b, N, m1, M1, eps)