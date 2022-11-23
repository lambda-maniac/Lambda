# How to use the `Curry` class:
First, import the class `Curry` from the module `Curry`:
```py
from Curry import Curry
```
then, decorate any function you want to curry, ex:
```py
@Curry
def add(a, b):
    return a + b
```
and now, the function `add` is curried, simple as that. Usage:
```py
>>> add (5)
'<Curried add [5]>'

>>> add (5) (5)
10

>>> increment = add (1)
>>> increment
'<Curried add [1]>'

>>> increment (1)
2
```

# Pipe'ing arguments:
Any functions that is decorated with the `Curry` class, also accepts arguments via pipe syntax, this means that:
```py
>>> 5 | add (5)
10
```
is valid, so you can chain functions.

# Right-to-left applications:
If, what you need, is to 'chain arguments', you should use `**` (exponent operator), as it is right-associative, ex:
```py
>>> 5 ** 5 ** add # Same as: 5 | (5 | add)
10
```
this is valid, because the expression is read right-to-left. This couldn't be done with `|` (or operator), as it is left-associative.

# Cleaner applications:
Tired of parenthesis? Use `&` (bitwise-and operator), the function application, but be careful, it is only suitable on the last argument of a function, otherwise, you'll need parenthesis anyway, ex:
```py
>>> increment& 1
2
```

# Full examples:
```
# Squaring a list

from Curry    import Curry
from Function import List

square  = Curry (lambda n: n ** 2)
numbers = [1, 2, 3, 4, 5]

squared_numbers = numbers \
                | List.Map& square
```
