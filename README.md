# Currying
Import the `Curry` class, located in `Currying.py`:
```py
from Lambda.Prelude.Currying import Curry
```
Then, decorate any function with the class `Curry`:
```py
@Curry # Defined in Lambda.Prelude.Operator @ Add
def Add(a, b):
    """:: a -> a -> a"""
    return a + b
```
Simple as that, now the function `Add` supports currying, here's some examples (from repl):
```py
>>> Add (5) (5) # Full application
10
```
```py
>>> Add (5) # Partial application
'<Curried Add [5]>'
```
```py
>>> inc = Add (1)
>>> inc
'<Curried Add [1]>'
>>> inc (5)
6
```

# The "function application" functions:
Any function that is curried, also accepts two special syntaxes that allows you to pipe arguments in, from the left, or from the right:
> Left application:
> ```py
> 5 | Add
> ```
> Right application:
> ```py
> Add & 5
> ```
Both of the examples above are equal to:
```py
Add (5)
```

# The "function composition" functions:
Any function `f` and `g` that are curried, and the return type of `g` is the input type of `f`, then `f` and `g` are composeable. Take a look at the "function composition" function:
```py
@Curry # Defined in Lambda.Prelude.Combinator @ compose
def compose(f, g, a):
    """:: (a -> b) -> (b -> c) -> a -> c"""
    return f& (g& a)
```
Function composition also has two special syntaxes:
> Right-associative:
> ```py
> f ** g # Apply f after applying g
> ```
> Left-associative:
> ```py
> f @ g # Apply f then apply g
> ```
Where `@` is just a flipped version of `**`.

# Infix functions:
Any functions that is curried, can also be infix, if placed between `|` and `&`, Ex (from repl):
```py
>>> 5 | Add & 5
10
```
```py
>>> from Lambda.Prelude.Combinator import amalgamation
>>> from Lambda.Prelude.List       import zip, tail
>>> sections = tail | amalgamation & zip
>>> sections
'<Curried amalgamation [<Curried zip []>, <Curried tail []>]>'
>>> sections& [1, 2, 3]
[(1, 2), (2, 3)]
```
