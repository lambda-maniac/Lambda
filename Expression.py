from Curry import Curry

@Curry
def defer(value, b_return):
    return (value, b_return)

@Curry
def switch(value, branches):
    for (b_value, b_return) in branches:
        if value == b_value: return b_return

    return None
