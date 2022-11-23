""" =====================================
::: Operations defined using Curry class.
===================================== """

from Curry import Curry

class Operator:

    @Curry
    @staticmethod
    def Add(a, b):
        return a + b

    @Curry
    @staticmethod
    def Mul(a, b):
        return a * b

    @Curry
    @staticmethod
    def Sub(a, b):
        return a - b

    @Curry
    @staticmethod
    def Div(a, b):
        return a / b

    @Curry
    @staticmethod
    def And(a, b):
        return a and b

    @Curry
    @staticmethod
    def Or(a, b):
        return a or b

    @Curry
    @staticmethod
    def In(a, b):
        return a in b

class List:

    @Curry
    @staticmethod
    def Map(function, elements):
        return [ function& element for element in elements ]

    @Curry
    @staticmethod
    def Foldl(function, accumulator, elements):
        for element in elements:
            accumulator = function& accumulator& element

        return accumulator

    @Curry
    @staticmethod
    def Foldr(function, accumulator, elements):
        for element in elements:
            accumulator = function& element& accumulator

        return accumulator

    @Curry
    @staticmethod
    def Filter(predicate, elements):
        return [ element for element in elements if predicate& element ]

    @Curry
    @staticmethod
    def Sum(elements): # Sum Monoid
        return elements \
             | List.Foldl& Operator.Add& 0

    @Curry
    @staticmethod
    def Product(elements): # Product Monoid
        return elements \
             | List.Foldl& Operator.Mul& 1

    @Curry
    @staticmethod
    def Any(elements): # Disjunction Monoid
        return elements \
             | List.Foldl& Operator.Or& False
    @Curry
    @staticmethod
    def All(elements): # Conjunction Monoid
        return elements \
             | List.Foldl& Operator.And& True
