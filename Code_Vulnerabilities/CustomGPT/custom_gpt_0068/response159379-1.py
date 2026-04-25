
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Your logic for equality check

    def __hash__(self):
        return hash(id(self))  # Unique hash based on object id

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # Output: False
print(hash(obj1))    # Outputs the hash of obj1
