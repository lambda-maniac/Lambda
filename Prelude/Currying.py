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

    def __ror__ (self, argument): return self(argument) # left  associative
    def __and__ (self, argument): return self(argument) # clean application
    def __pow__ (self, function):

        @Curry
        def composition(f, g, a):
            return f& (g& a)

        return composition& self& function

    def __matmul__(self, function):
        return function.__pow__(self)

    def __or__(self, function):
        if isinstance(function, Curry):
            return function(self)

        raise Exception(f"{function.__class__} is not pipeable.")

    def __repr__(self):
        return f'<Curried {self.function.__name__} {self.arguments}>'
