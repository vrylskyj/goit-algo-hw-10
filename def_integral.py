import random
from scipy.integrate import quad

def monte_carlo_integration(f, a, b, n):
    total = 0
    for _ in range(n):
        x = random.uniform(a, b)
        total += f(x)
    return total * (b - a) / n

def f(x):
    return x ** 3

a = 0
b = 1
n = 10000

result = monte_carlo_integration(f, a, b, n)
print("Monte Carlo Integration Result:", result)

analytical_result, _ = quad(f, a, b)
print("Analytical Integration Result:", analytical_result)

error = abs(result - analytical_result)
print("Absolute Error:", error)