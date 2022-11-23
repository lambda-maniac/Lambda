from Curry import Curry

@Curry
def Add(a, b):
    return a + b

@Curry
def Mul(a, b):
    return a * b

@Curry
def Sub(a, b):
    return a - b

@Curry
def Div(a, b):
    return a / b

@Curry
def And(a, b):
    return a and b

@Curry
def Or(a, b):
    return a or b

@Curry
def In(a, b):
    return a in b
