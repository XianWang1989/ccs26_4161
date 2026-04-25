
#!/usr/bin/python3

class MyClass:
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # or any proper equality condition
        return NotImplemented

    def __hash__(self):
        return hash(())  # Return a constant hash or based on attributes if any

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # This will invoke __eq__
print(hash(obj1))    # This will invoke __hash__
