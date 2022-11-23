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
```
```py
>>> add (5) (5)
10
```
```py
>>> increment = add (1)
>>> increment
'<Curried add [1]>'
```
```py
>>> increment (1)
2
```

# Pipe'ing arguments:
Any functions that is decorated with the `Curry` class, also accepts arguments via pipe syntax, this means that:
```py
>>> 5 | add (5)
10
```
is valid, so you can chain functions. (This is just a flipped function application `&`)

# Cleaner applications:
Tired of parenthesis? Use `&` (bitwise-and operator), the function application.
```py
>>> add& 5& 5
10
```

# Function composition:
To compose functions, use `**` (exponent operator), but, be aware that it is right-associative, so composition happens right-to-left:
```py
>>> from Operator import Add, Mul
>>> add5 = Add& 5
>>> mul5 = Mul& 5
>>> add5 ** mul5 & 5
30
>>> mul5 ** add5 & 5
50
```

# Full examples:
```py
# Squaring a list

from Curry import Curry

import List

square  = Curry (lambda n: n ** 2)
numbers = [1, 2, 3, 4, 5]

squared_numbers = numbers \
                | List.Map& square
```
```py
# Replacing all elements of a list with 0

import List
import Combinator

numbers = [1, 2, 3, 4, 5]
zeros   = numbers \
        | List.Map& (Combinator.Const& 0)
```
```py
# Adding two lists together

import List
import Operator

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

sum = List.ZipWith& Operator.Add& a& b
```
