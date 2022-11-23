from Curry      import Curry
from Combinator import Uncurry
from Operator   import Add, Mul, Or, And

@Curry
def Map(function, elements):
    return [ function& element for element in elements ]

@Curry
def Zip(list_a, list_b):
    return [ (list_a[index], list_b[index]) for index in range(len(list_a)) ]

@Curry
def ZipWith(function, list_a, list_b):
    return Zip& list_a& list_b \
         | Map& (Uncurry& function)

@Curry
def Foldl(function, accumulator, elements):
    for element in elements:
        accumulator = function& accumulator& element

    return accumulator

@Curry
def Foldr(function, accumulator, elements):
    for element in elements:
        accumulator = function& element& accumulator

    return accumulator

@Curry
def Filter(predicate, elements):
    return [ element for element in elements if predicate& element ]

@Curry
def Sum(elements): # Sum Monoid
    return elements \
         | Foldl& Add& 0

@Curry
def Product(elements): # Product Monoid
    return elements \
         | Foldl& Mul& 1

@Curry
def Any(elements): # Disjunction Monoid
    return elements \
         | Foldl& Or& False
@Curry
def All(elements): # Conjunction Monoid
    return elements \
         | Foldl& And& True
