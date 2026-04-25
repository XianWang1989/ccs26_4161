
def foo(row, f, **kwargs):
    if callable(f):
        return f(**{**kwargs, **{key: row[idx] for key, idx in kwargs.items()}})
    elif isinstance(f, str):
        return f
    else:
        return row[f]
