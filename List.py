from Curry      import Curry
from Combinator import uncurry, amalgamation
from Operator   import Add, Mul, Or, And

@Curry
def head(elements):
    """:: [a] -> a"""
    return elements[0]

@Curry
def tail(elements):
    """:: [a] -> [a]"""
    return elements[1:]

@Curry
def last(elements):
    """:: [a] -> a"""
    return elements[-1]

@Curry
def init(elements):
    """:: [a] -> [a]"""
    return elements[:-1]

@Curry
def reverse(elements):
    """:: [a] -> [a]"""
    return elements[::-1]

@Curry
def map(function, elements):
    """:: (a -> b) -> [a] -> [b]"""
    return [ function& element for element in elements ]

@Curry
def zip(list_a, list_b):
    """:: [a] -> [b] -> [(a, b)]"""
    return [ (list_a[index], list_b[index]) for index in range(min(len(list_a), len(list_b))) ]

@Curry
def zip_with(function, list_a, list_b):
    """:: (a -> b -> c) -> [a] -> [b] -> [c]"""
    return zip& list_a& list_b \
         | map& (uncurry& function)

@Curry
def foldl(function, accumulator, elements):
    """:: (b -> a -> b) -> b -> [a] -> b"""
    for element in elements:
        accumulator = function& accumulator& element

    return accumulator

@Curry
def foldr(function, accumulator, elements):
    """:: (a -> b -> b) -> b -> [a] -> b"""
    for element in elements:
        accumulator = function& element& accumulator

    return accumulator

@Curry
def filter(predicate, elements):
    """:: (a -> Bool) -> [a] -> [a]"""
    return [ element for element in elements if predicate& element ]

@Curry
def group(elements):
    """:: [a] -> [[a]]"""
    length = len(elements)

    if length == 0: return []
    if length == 1: return [elements]

    n_elements = []
    grouping   = []

    for (x, y) in amalgamation (zip) (tail) & elements:

        grouping.append(x)

        if x != y:
            n_elements.append(grouping)
            grouping = []

    return n_elements

@Curry
def concat(elements):
    """:: [[a]] -> [a]"""
    return [ element for sub_elements in elements for element in sub_elements ]

@Curry
def concat_with(function, elements):
    """:: ([a] -> [b]) -> [[a]] -> [b]"""
    return map (function) @ concat & elements

@Curry
def sum(elements): # Sum Monoid
    """:: Num a => [a] -> a"""
    return elements \
         | foldl& Add& 0

@Curry
def product(elements): # Product Monoid
    """:: Num a => [a] -> a"""
    return elements \
         | foldl& Mul& 1

@Curry
def any(elements): # Disjunction Monoid
    """:: [Bool] -> Bool"""
    return elements \
         | foldl& Or& False
@Curry
def all(elements): # Conjunction Monoid
    """:: [Bool] -> Bool"""
    return elements \
         | foldl& And& True
