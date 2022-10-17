import sympy as sym
from sympy import symbols, diff, S, Interval, latex
from sympy.solvers import solve, nsolve, solveset
from sympy.plotting import plot
from sympy import cos, sin, pi

sym.init_printing(use_latex = 'mathjax')
x = symbols('x')

Func = -12*x**4 * sin(cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

solve_set = set([nsolve(Func,n) for n in range(-5,6)])

print(solve_set)