from . Currying import Curry

@Curry
def Add(a, b):
    """:: a -> a -> a"""
    return a + b

@Curry
def Mul(a, b):
    """:: a -> a -> a"""
    return a * b

@Curry
def Sub(a, b):
    """:: a -> a -> a"""
    return a - b

@Curry
def Div(a, b):
    """:: a -> a -> a"""
    return a / b

@Curry
def Pow(a, b):
    """:: a -> a -> a"""
    return a ** b

@Curry
def Mat(a, b):
    """:: a -> a -> a"""
    return a @ b

@Curry
def And(a, b):
    """:: a -> a -> a"""
    return a and b

@Curry
def Or(a, b):
    """:: a -> a -> a"""
    return a or b

@Curry
def bAnd(a, b):
    """:: a -> a -> a"""
    return a & b

@Curry
def bOr(a, b):
    """:: a -> a -> a"""
    return a | b

@Curry
def In(a, b):
    """:: a -> b -> Bool"""
    return a in b

@Curry
def Eq(a, b):
    """:: a -> b -> Bool"""
    return a == b

@Curry
def Ne(a, b):
    """:: a -> b -> Bool"""
    return a != b

@Curry
def Gt(a, b):
    """:: a -> b -> Bool"""
    return a > b

@Curry
def Lt(a, b):
    """:: a -> b -> Bool"""
    return a < b

@Curry
def Ge(a, b):
    """:: a -> b -> Bool"""
    return a >= b

@Curry
def Le(a, b):
    """:: a -> b -> Bool"""
    return a <= b
