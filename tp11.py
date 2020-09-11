"""
TP -- Recursivite
"""

def u(n):
    if n==0:
        return 6
    return u(n-1)+3

def v(n):
    if n==0:
        return 20
    return v(n-1)+5

def w(n):
    if n==0:
        return 5000
    return w(n-1)*2

def x(n):
    if n==0:
        return 2
    return w(n-1)*0.3

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return f(n-1)+f(n-2)

def succ(n):
    if n==0:
        return 1
    return succ(n-1)+1

def baton(n):
    if n==0:
        return ""
    return "I"+baton(n-1)

def puissance(a, n):
    if n==0:
        return 1
    return a*puissance(n-1)

def somme(n):
    if n==0:
        return 0
    return n+somme(n-1)
