
# Define your functions that may return a value
def foo():
    # logic for foo
    return None  # or return some value

def bar():
    # logic for bar
    return None  # or return some value

def baz():
    # logic for baz
    return None  # or return some value

# Use a generator expression with next
result = next((var for func in (foo, bar, baz) if (var := func())), None)

# result now contains the first truthy value returned by `foo`, `bar`, or `baz`.
