
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)
