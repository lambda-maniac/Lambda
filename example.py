# Check which name has more occurences, John or Jane.

from Curry      import Curry
from Expression import switch, defer

import List
import Combinator

names = ["John", "Jane", "John", "Jane", "Jane", "John", "John"]

name_to_num = Curry (
    lambda name:
        switch &name& [
            defer &"John"&  1,
            defer &"Jane"& -1,
        ]
)

num_to_name = Curry (
    lambda number:
        switch &number& [
            defer &  1 & "John",
            defer & -1 & "Jane",
        ]
)

signum = Curry (
    lambda number:
        -1 if number < 0 else
         1 if number > 0 else
         0
)

names_to_num = List.Map& name_to_num

who_has_more_occurences = num_to_name ** signum ** List.Sum ** names_to_num

print (
    f"{who_has_more_occurences& names} has more occurences."
)
