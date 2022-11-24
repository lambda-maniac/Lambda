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
# "Function application" functions:
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
