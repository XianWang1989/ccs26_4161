
#!/usr/bin/python3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        return id(self)  # or any constant value if hashes do not need uniqueness

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # Outputs: False
print(hash(obj1))    # Outputs the hash of obj1
