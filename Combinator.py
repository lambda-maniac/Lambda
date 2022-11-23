from Curry import Curry

@Curry
def Id(a):
    """:: a -> a"""
    return a

@Curry
def Const(a, b):
    """:: a -> b -> a"""
    return a

@Curry
def Flip(function, b, a):
    """:: (a -> b -> c) -> b -> a -> c"""
    return function& a& b

@Curry
def Uncurry(function, a_and_b):
    """:: (a -> b -> c) -> (a, b) -> c"""
    a, b = a_and_b
    return function& a& b

@Curry
def Substitute(binary, unary, a):
    """:: (a -> b -> c) -> (a -> b) -> a -> c"""
    return binary& a& (unary& a)

@Curry
def Inbetween(a, b, function):
    """:: a -> b -> (a -> b -> c) -> c"""
    return function& a& b

@Curry
def Compose(f, g, a):
    """:: (a -> b) -> (b -> c) -> a -> c"""
    return f& (g& a)
