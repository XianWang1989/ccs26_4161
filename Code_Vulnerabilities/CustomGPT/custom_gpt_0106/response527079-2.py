
def funcToGetBar():
    # This is your actual implementation
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)
