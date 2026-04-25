
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False  # Define your equality logic here
        return NotImplemented

    def __hash__(self):
        return hash(False)  # Provide a consistent hash value

# Example usage
a = MyClass()
b = MyClass()
print(a == b)  # Outputs: False
