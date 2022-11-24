from . Curry import Curry

@Curry
def id(a):
    """:: a -> a"""
    return a

@Curry
def const(a, b):
    """:: a -> b -> a"""
    return a

@Curry
def flip(function, a, b):
    """:: (a -> b -> c) -> b -> a -> c"""
    return function& b& a

@Curry
def uncurry(function, a_and_b):
    """:: (a -> b -> c) -> (a, b) -> c"""
    a, b = a_and_b
    return function& a& b

@Curry
def amalgamation(binary, unary, a):
    """:: (a -> b -> c) -> (a -> b) -> a -> c"""
    return binary& a& (unary& a)

@Curry
def inbetween(a, b, function):
    """:: a -> b -> (a -> b -> c) -> c"""
    return function& a& b

@Curry
def compose(f, g, a):
    """:: (a -> b) -> (b -> c) -> a -> c"""
    return f& (g& a)
