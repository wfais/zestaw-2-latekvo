import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

def rysuj_wielomian(wejscie):
    funkcja_txt, zakres = wejscie.split(',')
    funkcja_txt = funkcja_txt.strip()
    x_min, x_max = map(float, zakres.strip().split())
    x_val = np.linspace(x_min, x_max, 200)
    y_val = np.array([eval(funkcja_txt, {"x": xv, "np": np}) for xv in x_val])
    plt.figure()
    plt.plot(x_val, y_val)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Wielomian eval")
    plt.grid(True)
    return y_val[0], y_val[-1]

def rysuj_wielomian_sympy(wejscie):
    funkcja_txt, zakres = wejscie.split(',')
    funkcja_txt = funkcja_txt.strip()
    x_min, x_max = map(float, zakres.strip().split())
    x = symbols('x')
    expr = sympify(funkcja_txt)
    f = lambdify(x, expr, "numpy")
    x_val = np.linspace(x_min, x_max, 200)
    y_val_sympy = f(x_val)
    plt.figure()
    plt.plot(x_val, y_val_sympy)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Wielomian SymPy")
    plt.grid(True)
    return float(y_val_sympy[0]), float(y_val_sympy[-1])

if __name__ == '__main__':
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)

    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)

    plt.show()

