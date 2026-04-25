
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Implement your equality logic here

    def __hash__(self):
        return hash(id(self))  # Provide a hash implementation

# Example usage
a = MyClass()
b = MyClass()
print(a == b)  # Outputs: False
