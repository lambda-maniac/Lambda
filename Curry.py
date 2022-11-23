""" ==========
::: Main code.
========== """

from inspect import signature

class Curry:
    def __init__(self, function, arguments = [], argument_count = -1):
        self.function       = function
        self.arguments      = arguments
        self.argument_count = argument_count       \
                           if argument_count != -1 \
                         else len ( signature(function).parameters )

    def __call__(self, argument):

        n_arguments = self.arguments      + [argument]
        n_length    = self.argument_count - 1

        if n_length <= 0: return self.function(*n_arguments)

        return Curry(self.function, n_arguments, n_length)

    def  __ror__ (self, argument): return self(argument) # left  associative
    def __rpow__ (self, argument): return self(argument) # right associative
    def  __and__ (self, argument): return self(argument) # clean application

    def __repr__(self):
        return f'<Curried {self.function.__name__} {self.arguments}>'

""" ========
::: Aliases.
======== """

curry   = Curry
uncurry = lambda curried: curried.function
