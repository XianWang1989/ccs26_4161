
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False
        return NotImplemented

    def __hash__(self):
        return hash(id(self))

# Example usage
obj1 = MyClass()
obj2 = MyClass()
print(obj1 == obj2)  # Outputs: False
