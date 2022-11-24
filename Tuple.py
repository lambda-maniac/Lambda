from Curry import Curry

@Curry
def pair(a, b):
    """:: a -> b -> (a, b)"""
    return (a, b)

@Curry
def first(f, a_and_c):
    """:: (a -> b) -> (a, c) -> (b, c)"""
    a, c = a_and_c

    return (f& a, c)

@Curry
def second(f, c_and_a):
    """:: (a -> b) -> (c, a) -> (c, b)"""
    c, a = c_and_a

    return (c, f& a)

@Curry
def both(f, a_and_a):
    """:: (a -> b) -> (a, a) -> (b, b)"""
    x, y = a_and_a

    return pair (f& x) (f& y)

@Curry
def build_from(f, g, a):
    """:: (a -> b) -> (a -> c) -> a -> (b, c)"""
    return (f& a, g& a)
