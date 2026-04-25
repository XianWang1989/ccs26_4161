
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        return hash(id(self))  # or another implementation based on your class properties
