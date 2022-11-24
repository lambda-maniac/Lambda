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
is valid, so you can chain functions. (This is just a flipped "function application" function `&`)

# Cleaner applications:
Tired of parenthesis? Use `&` (bitwise-and operator), the "function application" function.
```py
>>> add& 5& 5
10
```

# Infix functions.
If you haven't noticed yet, placing a function in between the two "function application" functions, a.k.a. `|` and `&` (where Pipe/Or is just a flipped And), will have the same effect as having that same function, but infix.
```py
>>> 5 |add& 5
10
```

# Right-to-left function composition:
To compose functions, right-to-left, use `**` (exponent operator):
```py
>>> from Operator import Add, Mul
>>> Add (5) ** Mul (5) & 5 # 'Add 5 after Mul 5'
30
>>> Mul (5) ** Add (5) & 5 # 'Mul 5 after Add 5'
50
```

# Left-to-right function composition:
To compose functions, left-to-right, use `@` (matmul operator):
```py
>>> from Operator import Add, Mul
>>> Add (5) @ Mul (5) & 5 # 'Add 5 then Mul 5'
50
>>> Mul (5) @ Add (5) & 5 # 'Mul 5 then Add 5'
30
```

# Full examples:
```py
# Finding the sum of squares

from Curry import Curry

import List

square  = Curry (lambda n: n ** 2)
numbers = [1, 2, 3, 4, 5]
result  = numbers          \
        | List.Map& square \
        | List.Sum
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
