
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        # Return a hash value, for example, 0 (or any other consistent value)
        return 0
