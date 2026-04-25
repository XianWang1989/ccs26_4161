
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        return id(self)

# Example usage
obj1 = MyClass()
obj2 = MyClass()
print(obj1 == obj2)  # Should print False
