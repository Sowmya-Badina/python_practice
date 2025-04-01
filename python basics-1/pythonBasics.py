# Modules and pip
#built in modules and external modules
# in cmd prompt, pip install pandas
import pandas as pd

A=int(input('Enter First Number:'))
B=int(input('Enter Second Number:'))

def add(A,B):
    return A+B

def sub(A,B):
    return A-B

def multiply(A,B):
    return A*B

def division(A,B):
    return A/B

def fd(A,B):
    return A//B

def mod(A,B):
    return A%B

def exp(A,B):
    return A**B

def cal(A,B):
    print(add(A,B))
    print(sub(A,B))
    print(multiply(A,B))
    print(division(A,B))
    print(fd(A,B))
    print(mod(A,B))
    print(exp(A,B))

cal(A,B)


