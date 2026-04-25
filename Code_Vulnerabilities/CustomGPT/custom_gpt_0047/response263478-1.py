
from collections import namedtuple
from typing import Callable, Any, List, Dict

# Define a namedtuple to specify function calls
FunctionCall = namedtuple('FunctionCall', ['function', 'args'])

def foo(row: List[Any], call: FunctionCall) -> Any:
    # Construct the arguments based on the specified indices and static values
    args = []
    for arg in call.args:
        if isinstance(arg, int):
            args.append(row[arg])
        else:
            args.append(arg)
    return call.function(*args)

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b):
    return a * b

# Example dataset
data_row = [5, 10, 15, 20]

# Function calls
fList = [
    FunctionCall(func1, [0, 1, 2]),  # Uses elements 5, 10, 15 from data_row
    FunctionCall(func2, [1, 2]),     # Uses elements 10, 15 from data_row
    FunctionCall(lambda x, y: x + y + '!', ['World', 2])  # Static and dynamic args
]

# Running the functions
for call in fList:
    print(foo(data_row, call))
