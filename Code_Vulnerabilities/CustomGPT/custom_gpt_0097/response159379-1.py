
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False
        return NotImplemented

    def __hash__(self):
        return hash((self.__class__,))
