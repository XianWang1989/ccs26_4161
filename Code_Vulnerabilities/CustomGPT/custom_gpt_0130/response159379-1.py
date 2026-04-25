
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # or your actual equality logic

    def __hash__(self):
        return hash(id(self))  # or use a specific attribute for consistent hashing
