from .. Curry import Curry
from .. Tuple import pair

defer = pair

@Curry
def switch(value, branches):
    for (b_value, b_return) in branches:
        if value == b_value: return b_return

    return None
