import math
def factorial(e):
    if e == 0 or e == 1:
        return 1
    else:
        return e * factorial(e - 1)
print(factorial(10))
def sine_x(x, n):
    x = math.radians(x)
    term = lambda n: ((-1) * n * x * (2 * n + 1)) / factorial(2 * n + 1)
    last = 0

    for i in range(n):
        curr = term(i)
        last += curr
    return last

print(sine_x(5,10))
hsum = 0  # for global
def harmonic(n):
    global hsum
    if n == 0:
        return
    harmonic(n - 1)
    hsum += 1 / n

harmonic(5)
print(hsum)



