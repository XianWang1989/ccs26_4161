
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        # Provide a meaningful equality check (example)
        return isinstance(other, MyClass)

    def __hash__(self):
        # Return a hash value (example)
        return hash(type(self))

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # Should return True if comparing same types
print(hash(obj1))    # Should return a hash value
