
#!/usr/bin/python3

class MyClass:
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        # Return a hash value; use a constant or relevant attributes
        return hash(0)

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # Outputs: False
print(hash(obj1))    # Outputs: 0
