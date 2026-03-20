import numpy as np

def f(x):
    return x**3 + 2*x**2 - 5*x + 1 

def gradient_numerisch(f, x, h=1e-5):
    abt_f = (f(x+h)-f(x-h))/(2*h)
    return abt_f


punkten = np.array([0, 1, 2, 3])
for x in punkten:
    grad = gradient_numerisch(f, x)
    print(f"f'({x}) ≈ {grad:.4f}")